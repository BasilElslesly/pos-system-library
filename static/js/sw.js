// Service Worker للعمل بدون إنترنت
const CACHE_NAME = 'pos-system-v1';
const urlsToCache = [
    '/',
    '/pos',
    '/sales',
    '/purchases',
    '/products',
    '/customers',
    '/suppliers',
    '/reports',
    '/returns',
    '/static/css/bootstrap.min.css',
    '/static/js/bootstrap.bundle.min.js',
    '/static/js/chart.js',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css'
];

// تثبيت Service Worker
self.addEventListener('install', function(event) {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function(cache) {
                console.log('تم فتح الكاش');
                return cache.addAll(urlsToCache);
            })
    );
});

// اعتراض الطلبات
self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request)
            .then(function(response) {
                // إرجاع الاستجابة من الكاش إذا وجدت
                if (response) {
                    return response;
                }

                return fetch(event.request).then(
                    function(response) {
                        // التحقق من صحة الاستجابة
                        if(!response || response.status !== 200 || response.type !== 'basic') {
                            return response;
                        }

                        // نسخ الاستجابة
                        var responseToCache = response.clone();

                        caches.open(CACHE_NAME)
                            .then(function(cache) {
                                cache.put(event.request, responseToCache);
                            });

                        return response;
                    }
                ).catch(function() {
                    // إرجاع صفحة بديلة في حالة عدم وجود اتصال
                    if (event.request.destination === 'document') {
                        return caches.match('/');
                    }
                });
            })
    );
});

// تحديث Service Worker
self.addEventListener('activate', function(event) {
    var cacheWhitelist = [CACHE_NAME];

    event.waitUntil(
        caches.keys().then(function(cacheNames) {
            return Promise.all(
                cacheNames.map(function(cacheName) {
                    if (cacheWhitelist.indexOf(cacheName) === -1) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});

// مزامنة البيانات في الخلفية
self.addEventListener('sync', function(event) {
    if (event.tag === 'background-sync') {
        event.waitUntil(doBackgroundSync());
    }
});

function doBackgroundSync() {
    return fetch('/api/system/sync', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    }).then(function(response) {
        console.log('تمت المزامنة في الخلفية');
        return response;
    }).catch(function(error) {
        console.log('فشلت المزامنة في الخلفية:', error);
        throw error;
    });
}

// إشعارات Push
self.addEventListener('push', function(event) {
    const options = {
        body: event.data ? event.data.text() : 'إشعار من نظام نقطة البيع',
        icon: '/static/images/icon-192x192.png',
        badge: '/static/images/badge-72x72.png',
        vibrate: [100, 50, 100],
        data: {
            dateOfArrival: Date.now(),
            primaryKey: 1
        },
        actions: [
            {
                action: 'explore',
                title: 'فتح النظام',
                icon: '/static/images/checkmark.png'
            },
            {
                action: 'close',
                title: 'إغلاق',
                icon: '/static/images/xmark.png'
            }
        ]
    };

    event.waitUntil(
        self.registration.showNotification('نظام نقطة البيع', options)
    );
});

// التعامل مع النقر على الإشعارات
self.addEventListener('notificationclick', function(event) {
    event.notification.close();

    if (event.action === 'explore') {
        event.waitUntil(
            clients.openWindow('/')
        );
    }
});
