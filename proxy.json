{
  "burstObservatory" : {
    "pingConfig" : {
      "connectivity" : "",
      "destination" : "http:\/\/www.gstatic.com\/generate_204",
      "interval" : "10m",
      "sampling" : 3,
      "timeout" : "5s"
    },
    "subjectSelector" : [
      "proxy"
    ]
  },
  "dns" : {
    "queryStrategy" : "UseIPv4",
    "servers" : [
      {
        "address" : "localhost",
        "domains" : [
          "domain:ru",
          "domain:su",
          "domain:xn--p1ai",
          "domain:yandex.net",
          "domain:yastatic.net",
          "domain:vk.com",
          "domain:userapi.com"
        ]
      },
      "https:\/\/8.8.8.8\/dns-query",
      "https:\/\/77.88.8.8\/dns-query"
    ]
  },
  "inbounds" : [
    {
      "listen" : "127.0.0.1",
      "port" : 10808,
      "protocol" : "socks",
      "settings" : {
        "allowTransparent" : false,
        "auth" : "noauth",
        "udp" : true
      },
      "sniffing" : {
        "destOverride" : [
          "http",
          "tls"
        ],
        "enabled" : true,
        "routeOnly" : false
      },
      "tag" : "socks"
    },
    {
      "listen" : "127.0.0.1",
      "port" : 10809,
      "protocol" : "http",
      "settings" : {
        "allowTransparent" : false,
        "auth" : "noauth",
        "udp" : true
      },
      "sniffing" : {
        "destOverride" : [
          "http",
          "tls"
        ],
        "enabled" : true,
        "routeOnly" : false
      },
      "tag" : "http"
    }
  ],
  "log" : {
    "access" : "\/private\/var\/mobile\/Containers\/Shared\/AppGroup\/66B561C9-9965-49BA-9EA8-D5C9CACADD2B\/Library\/Application Support\/Xray\/logs\/access.log",
    "dnsLog" : true,
    "loglevel" : "Warning"
  },
  "outbounds" : [
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "de1-7.itray.net",
            "port" : 443,
            "users" : [
              {
                "alterId" : 0,
                "email" : "https:\/\/gozargah.github.io\/marzban\/",
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "175d3977-0f2b-4629-a1d3-3fe35c9c3c51",
                "security" : "auto"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "firefox",
          "publicKey" : "kBTMVLCNE0jjwuJF6H5-65l5Pe0QToS0Hg-9Tmaa7Sk",
          "serverName" : "images.porsche.com",
          "shortId" : "1a2b3c4d",
          "show" : false
        },
        "security" : "reality"
      },
      "tag" : "proxy"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "de1-2.itray.net",
            "port" : 443,
            "users" : [
              {
                "alterId" : 0,
                "email" : "https:\/\/gozargah.github.io\/marzban\/",
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "175d3977-0f2b-4629-a1d3-3fe35c9c3c51",
                "security" : "auto"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "firefox",
          "publicKey" : "kBTMVLCNE0jjwuJF6H5-65l5Pe0QToS0Hg-9Tmaa7Sk",
          "serverName" : "images.porsche.com",
          "shortId" : "1a2b3c4d",
          "show" : false
        },
        "security" : "reality"
      },
      "tag" : "proxy-2"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "de1-6.itray.net",
            "port" : 443,
            "users" : [
              {
                "alterId" : 0,
                "email" : "https:\/\/gozargah.github.io\/marzban\/",
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "175d3977-0f2b-4629-a1d3-3fe35c9c3c51",
                "security" : "auto"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "firefox",
          "publicKey" : "kBTMVLCNE0jjwuJF6H5-65l5Pe0QToS0Hg-9Tmaa7Sk",
          "serverName" : "images.porsche.com",
          "shortId" : "1a2b3c4d",
          "show" : false
        },
        "security" : "reality"
      },
      "tag" : "proxy-3"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "de1-4.itray.net",
            "port" : 443,
            "users" : [
              {
                "alterId" : 0,
                "email" : "https:\/\/gozargah.github.io\/marzban\/",
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "175d3977-0f2b-4629-a1d3-3fe35c9c3c51",
                "security" : "auto"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "firefox",
          "publicKey" : "kBTMVLCNE0jjwuJF6H5-65l5Pe0QToS0Hg-9Tmaa7Sk",
          "serverName" : "images.porsche.com",
          "shortId" : "1a2b3c4d",
          "show" : false
        },
        "security" : "reality"
      },
      "tag" : "proxy-4"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "de1-8.itray.net",
            "port" : 443,
            "users" : [
              {
                "alterId" : 0,
                "email" : "https:\/\/gozargah.github.io\/marzban\/",
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "175d3977-0f2b-4629-a1d3-3fe35c9c3c51",
                "security" : "auto"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "firefox",
          "publicKey" : "kBTMVLCNE0jjwuJF6H5-65l5Pe0QToS0Hg-9Tmaa7Sk",
          "serverName" : "images.porsche.com",
          "shortId" : "1a2b3c4d",
          "show" : false
        },
        "security" : "reality"
      },
      "tag" : "proxy-5"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "de1-10.itray.net",
            "port" : 443,
            "users" : [
              {
                "alterId" : 0,
                "email" : "https:\/\/gozargah.github.io\/marzban\/",
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "175d3977-0f2b-4629-a1d3-3fe35c9c3c51",
                "security" : "auto"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "firefox",
          "publicKey" : "kBTMVLCNE0jjwuJF6H5-65l5Pe0QToS0Hg-9Tmaa7Sk",
          "serverName" : "images.porsche.com",
          "shortId" : "1a2b3c4d",
          "show" : false
        },
        "security" : "reality"
      },
      "tag" : "proxy-6"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "de1-5.itray.net",
            "port" : 443,
            "users" : [
              {
                "alterId" : 0,
                "email" : "https:\/\/gozargah.github.io\/marzban\/",
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "175d3977-0f2b-4629-a1d3-3fe35c9c3c51",
                "security" : "auto"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "firefox",
          "publicKey" : "kBTMVLCNE0jjwuJF6H5-65l5Pe0QToS0Hg-9Tmaa7Sk",
          "serverName" : "images.porsche.com",
          "shortId" : "1a2b3c4d",
          "show" : false
        },
        "security" : "reality"
      },
      "tag" : "proxy-7"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "de1-1.itray.net",
            "port" : 443,
            "users" : [
              {
                "alterId" : 0,
                "email" : "https:\/\/gozargah.github.io\/marzban\/",
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "175d3977-0f2b-4629-a1d3-3fe35c9c3c51",
                "security" : "auto"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "firefox",
          "publicKey" : "kBTMVLCNE0jjwuJF6H5-65l5Pe0QToS0Hg-9Tmaa7Sk",
          "serverName" : "images.porsche.com",
          "shortId" : "1a2b3c4d",
          "show" : false
        },
        "security" : "reality"
      },
      "tag" : "proxy-8"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "de1-9.itray.net",
            "port" : 443,
            "users" : [
              {
                "alterId" : 0,
                "email" : "https:\/\/gozargah.github.io\/marzban\/",
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "175d3977-0f2b-4629-a1d3-3fe35c9c3c51",
                "security" : "auto"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "firefox",
          "publicKey" : "kBTMVLCNE0jjwuJF6H5-65l5Pe0QToS0Hg-9Tmaa7Sk",
          "serverName" : "images.porsche.com",
          "shortId" : "1a2b3c4d",
          "show" : false
        },
        "security" : "reality"
      },
      "tag" : "proxy-9"
    },
    {
      "protocol" : "vless",
      "settings" : {
        "vnext" : [
          {
            "address" : "de1-3.itray.net",
            "port" : 443,
            "users" : [
              {
                "alterId" : 0,
                "email" : "https:\/\/gozargah.github.io\/marzban\/",
                "encryption" : "none",
                "flow" : "xtls-rprx-vision",
                "id" : "175d3977-0f2b-4629-a1d3-3fe35c9c3c51",
                "security" : "auto"
              }
            ]
          }
        ]
      },
      "streamSettings" : {
        "network" : "tcp",
        "realitySettings" : {
          "fingerprint" : "firefox",
          "publicKey" : "kBTMVLCNE0jjwuJF6H5-65l5Pe0QToS0Hg-9Tmaa7Sk",
          "serverName" : "images.porsche.com",
          "shortId" : "1a2b3c4d",
          "show" : false
        },
        "security" : "reality"
      },
      "tag" : "proxy-10"
    },
    {
      "protocol" : "freedom",
      "tag" : "direct"
    }
  ],
  "remarks" : "🇩🇪 Germany #1⚡10 Gbit",
  "routing" : {
    "balancers" : [
      {
        "fallbackTag" : "proxy",
        "selector" : [
          "proxy"
        ],
        "strategy" : {
          "settings" : {
            "baselines" : [
              "80ms",
              "150ms",
              "300ms"
            ],
            "expected" : 2,
            "maxRTT" : "1500ms",
            "tolerance" : 0.050000000000000003
          },
          "type" : "leastLoad"
        },
        "tag" : "Auto_Balancer"
      }
    ],
    "domainMatcher" : "hybrid",
    "domainStrategy" : "IPIfNonMatch",
    "rules" : [
      {
        "ip" : [
          "127.0.0.0\/8",
          "10.0.0.0\/8",
          "172.16.0.0\/12",
          "192.168.0.0\/16",
          "169.254.0.0\/16",
          "100.64.0.0\/10"
        ],
        "outboundTag" : "direct",
        "type" : "field"
      },
      {
        "domain" : [
          "domain:ru",
          "domain:su",
          "domain:xn--p1ai",
          "domain:vk.com",
          "domain:userapi.com",
          "domain:mycdn.me",
          "domain:yandex.net",
          "domain:yandex.com",
          "domain:sberbank.com",
          "domain:gosuslugi.rt.ru"
        ],
        "outboundTag" : "direct",
        "type" : "field"
      },
      {
        "balancerTag" : "Auto_Balancer",
        "network" : "tcp,udp",
        "type" : "field"
      },
      {
        "network" : "tcp,udp",
        "outboundTag" : "proxy",
        "type" : "field"
      }
    ]
  }
}
