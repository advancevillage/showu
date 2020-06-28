# /usr/bin/env python
# -*- coding:utf-8 -*-

# pip install flask
from flask import abort, jsonify, Flask, request, Response, make_response

#百搭 joker
joker = [
    "http://www.starstyle.ph/wp-content/uploads/2019/11/Starstyle_Style-Stash_Maya-Nilsen8-1170x825.jpg",
    "http://image4.suning.cn/uimg/b2c/newcatentries/0070166958-000000000640627447_2_800x800.jpg",
    "https://pic.lady75.com/uploadfile/2014/1009/20141009034215221.jpg",
    "http://5b0988e595225.cdn.sohucs.com/images/20171022/aa529466536b4411bf69ca1d2301e27b.jpeg",
    "http://img1.cfw.cn/editors/attached/image/20170715/20170715145222832283.jpg",
    "http://www.tbw-xie.com/tuxieJDAxJDIyLzI0MjY3MDc4MzYvVEIyUEFwMmw1cG5wdUZqU1pGa1hYYzRacFhhXyEhMjQyNjcwNzgzNiQ5.jpg",
    "http://b1.hucdn.com/upload/item/1807/01/17891117066728_800x800.jpg",
    "http://img11.360buyimg.com/n1/s350x449_jfs/t14941/40/1111086908/186086/fcd097/5a44f100N2871380e.jpg%21cc_350x449.jpg",
    "http://image1.suning.cn/b2c/catentries/000000000149836725_1_800x800.jpg",
    "http://s11.mogucdn.com/mlcdn/55cf19/180610_0l17dj7ag28gh88hk7ea41lij077f_640x960.jpg"
]
#简约 minimalist
minimalist = [
    "https://imgf1.pop-fashion.com/upload/flash_report/2020/2020060913/ANAREPORT_5edf1c9edd5a3_2314.jpg",
    "http://5b0988e595225.cdn.sohucs.com/images/20170630/088fffd58c6746f88d67f7732a538b06.png",
    "https://imgf2.pop-fashion.com/upload/flash_report/2020/2020060316/ANAREPORT_5ed761518dd18_9238.jpg",
    "https://imgf2.pop-fashion.com/upload/flash_report/2020/2020052518/ANAREPORT_5ecb9c09163a1_8286.jpg",
    "https://imgf1.pop-fashion.com/upload/flash_report/2020/2020051216/ANAREPORT_5eba616e80bde_2641.jpg",
    "https://imgf2.pop-fashion.com/upload/flash_report/2020/2020051216/ANAREPORT_5eba60bf0a564_9063.jpg",
    "https://imgf2.pop-fashion.com/upload/flash_report/2020/2020041318/ANAREPORT_5e94432579b5a_4251.jpg",
    "https://imgf2.pop-fashion.com/upload/flash_report/2020/2020033117/ANAREPORT_5e83146d2b3dc_6881.png",
    "https://imgf2.pop-fashion.com/upload/flash_report/2020/2020031217/ANAREPORT_5e6a07b3b77fb_3829.jpg",
    "https://imgf2.pop-fashion.com/upload/flash_report/2020/2020012018/ANAREPORT_5e25822da2628_7396.jpg",
    "https://imgf1.pop-fashion.com/upload/flash_report/2020/2020011914/ANAREPORT_5e23f44392002_5090.jpg",
    "https://imgf1.pop-fashion.com/upload/flash_report/2020/2020011018/ANAREPORT_5e18573ccc08e_2157.jpg",
]

# 街头 Street
street = [
    "https://imgf2.pop-fashion.com/upload/flash_report/2020/2020061216/ANAREPORT_5ee33d89aed80_6574.jpg",
    "https://imgf1.pop-fashion.com/upload/flash_report/2020/2020043017/ANAREPORT_5eaa971649096_2987.jpg",
    "https://imgf2.pop-fashion.com/upload/flash_report/2020/2020040818/ANAREPORT_5e8da0d74d407_1568.jpg",
    "https://imgf2.pop-fashion.com/upload/flash_report/2020/2020040715/ANAREPORT_5e8c2f1b0b883_2795.jpg",
    "https://imgf2.pop-fashion.com/upload/flash_report/2019/2019082017/ANAREPORT_5d5bbd6879637_6261.jpg",
    "https://imgf3.pop-fashion.com/upload/flash_report/2019/2019081217/ANAREPORT_5d512ec765c03_5942.jpg",
    "https://imgf1.pop-fashion.com/upload/flash_report/2019/2019072918/ANAREPORT_5d3ec7441b87a_4708.jpg",
    "https://imgf3.pop-fashion.com/upload/flash_report/2019/2019072311/ANAREPORT_5d36854ea5709_6673.jpg",
    "https://imgf3.pop-fashion.com/upload/flash_report/2019/2019070914/ANAREPORT_5d2431e4251aa_7902.jpg",
    "https://imgf3.pop-fashion.com/upload/flash_report/2019/2019062417/ANAREPORT_5d109503539b0_8927.jpg"
]

korea = [
    "http://img007.hc360.cn/hb/6FK3706a95cac2c1c4D917D3ac4DDD4c354.jpg",
    "https://imgf2.pop-fashion.com/upload/flash_report/2019/2019031409/ANAREPORT_5c89b0b9857c2_5960.jpg",
    "https://imgf2.pop-fashion.com/upload/flash_report/2020/2020061113/ANAREPORT_5ee1bb8516b45_5365.gif",
    "https://imgf3.pop-fashion.com/upload/flash_report/2019/2019111313/ANAREPORT_5dcb9443cae95_8887.jpg",
    "https://imgf3.pop-fashion.com/upload/flash_report/2019/2019032610/ANAREPORT_5c998dc8c8f4a_7271.jpg",
    "https://imgf2.pop-fashion.com/upload/flash_report/2019/2019012617/ANAREPORT_5c4c27aa3a20f_3583.jpg",
    "https://imgf2.pop-fashion.com/upload/flash_report/2019/2019081717/ANAREPORT_5d57c7a7a469a_3442.jpg"
]

western = [
    "https://imgf2.pop-fashion.com/upload/flash_report/2020/2020060316/ANAREPORT_5ed761518dd18_9238.jpg",
    "https://imgf2.pop-fashion.com/upload/flash_report/2020/2020052518/ANAREPORT_5ecb9c09163a1_8286.jpg",
    "https://imgf1.pop-fashion.com/upload/flash_report/2020/2020050814/ANAREPORT_5eb4feb0ea8a5_8369.jpg",
    "https://imgf2.pop-fashion.com/upload/flash_report/2020/2020050718/ANAREPORT_5eb3dc216c9f5_8765.jpg",
    "https://imgf2.pop-fashion.com/upload/flash_report/2020/2020032419/ANAREPORT_5e79ea2b3646c_8794.jpg",
    "https://imgf3.pop-fashion.com/upload/flash_report/2020/2020032016/ANAREPORT_5e7479df81585_2517.jpg",
    "https://imgf1.pop-fashion.com/upload/flash_report/2020/2020031417/ANAREPORT_5e6ca6b33aa78_8826.jpg",
    "https://imgf1.pop-fashion.com/upload/flash_report/2020/2020031412/ANAREPORT_5e6c5b37b12ba_5413.jpg"
]

app = Flask(__name__)
# 增加配置，支持中文显示
app.config['JSON_AS_ASCII'] = False

notices = {
    "code": 200,
    "data": {
        "items": [
            {
                "value": "新品上市,开店打折",
                "link": "/list/",
                "icon": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg"
            },
            {
                "value": "物流查询",
                "link": "/",
                "icon": "https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3079830914,2496082776&fm=26&gp=0.jpg"
            },
        ],
        "total": 4
    }
}
@app.route('/v1/notices', methods=['GET'])
def get_notices():
    response = make_response(jsonify(notices))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response, 200


# https://api.softsun.com/v1/countries
# 国家(标准国家简称)-语言(i81)-符号(标准国家结算符号)
# CN-zh_CN-¥
# US-en-$
# country   国家
# currency  货币
# flag      国旗
# language  语言
countries = {
    "code": 200,
    "data": {
        "items": [
            {
                "country": "CN",
                "currency": "¥",
                "flag": "https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=209501257,179938329&fm=26&gp=0.jpg",
                "language": "zh_CN"
            },
            {
                "country": "US",
                "currency": "$",
                "flag": "https://img.ivsky.com/img/tupian/pre/201010/06/meiguo.png",
                "language": "en"
            },
        ],
        "total": 1
    }
}
@app.route('/v1/countries', methods=['GET'])
def get_countries():
    response = make_response(jsonify(countries))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response, 200

provinces = {
    "code": 200,
    "data": {
        "items": [
            {
                "value": "河北",
                 "cities": [
                     "保定", "石家庄"
                 ]
            },
            {
                "value": "内蒙古",
                "cities": [
                    "呼和浩特", "化德"
                ]
            },
            {
                "value": "Beijing",
                "cities": [
                    "Beijing"
                ]
            },
        ],
        "total": 1
    }
}

@app.route('/v1/provinces', methods=['GET'])
def get_provinces():
    response = make_response(jsonify(provinces))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response, 200


categories = {
    "code": 200,
    "data": {
        "items": [
            {
                "name": {
                    "en": "Summer",
                    "zh_CN": "夏装"
                },
                "banner": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589909869275&di=25ead44cab83131204f3b36ef9de513a&imgtype=0&src=http%3A%2F%2Fa2.att.hudong.com%2F36%2F48%2F19300001357258133412489354717.jpg", "link": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657341&di=e29b400824bb44c686795dd8531fa9a5&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F64%2F76%2F20300001349415131407760417677.jpg", "linke": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657436&di=b7d190c972effc30bc5f121ec86013bd&imgtype=0&src=http%3A%2F%2Ffile02.16sucai.com%2Fd%2Ffile%2F2015%2F0408%2F779334da99e40adb587d0ba715eca102.jpg", "link": "/"}
                ],
                "children": {
                    "women": [
                            {
                                "name": {
                                    "en": "T-Shirt",
                                    "zh_CN": "T恤"
                                },
                                "id": "cat-t-shirt",
                            },
                            {
                                "name": {
                                    "en": "T-Shirt",
                                    "zh_CN": "T恤"
                                },
                                "id": "cat-t-shirt",
                            },
                            {
                                "name": {
                                    "en": "T-Shirt",
                                    "zh_CN": "T恤"
                                },
                                "id": "cat-t-shirt",
                            },
                            {
                                "name": {
                                    "en": "T-Shirt",
                                    "zh_CN": "T恤"
                                },
                                "id": "cat-t-shirt",
                            },
                            {
                                "name": {
                                    "en": "T-Shirt",
                                    "zh_CN": "T恤"
                                },
                                "id": "cat-t-shirt",
                            },
                            {
                                "name": {
                                    "en": "T-Shirt",
                                    "zh_CN": "T恤"
                                },
                                "id": "cat-t-shirt",
                            },
                            {
                                "name": {
                                    "en": "T-Shirt",
                                    "zh_CN": "T恤"
                                },
                                "id": "cat-t-shirt",
                            },
                            {
                                "name": {
                                    "en": "T-Shirt",
                                    "zh_CN": "T恤"
                                },
                                "id": "cat-t-shirt",
                            },
                        ],
                    "man": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ],
                    "material": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ]
                },
                "id": "cat-summer"
            },
            {
                "name": {
                    "en": "Joker",
                    "zh_CN": "百搭"
                },
                "banner": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589909869275&di=25ead44cab83131204f3b36ef9de513a&imgtype=0&src=http%3A%2F%2Fa2.att.hudong.com%2F36%2F48%2F19300001357258133412489354717.jpg", "link": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657341&di=e29b400824bb44c686795dd8531fa9a5&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F64%2F76%2F20300001349415131407760417677.jpg", "linke": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657436&di=b7d190c972effc30bc5f121ec86013bd&imgtype=0&src=http%3A%2F%2Ffile02.16sucai.com%2Fd%2Ffile%2F2015%2F0408%2F779334da99e40adb587d0ba715eca102.jpg", "link": "/"}
                ],
                "children": {
                    "women": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ],
                    "man": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ],
                    "material": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ]
                },
                "id": "cat-joker"
            },
            {
                "name": {
                    "en": "Simple",
                    "zh_CN": "简约"
                },
                "banner": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589909869275&di=25ead44cab83131204f3b36ef9de513a&imgtype=0&src=http%3A%2F%2Fa2.att.hudong.com%2F36%2F48%2F19300001357258133412489354717.jpg", "link": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657341&di=e29b400824bb44c686795dd8531fa9a5&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F64%2F76%2F20300001349415131407760417677.jpg", "linke": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657436&di=b7d190c972effc30bc5f121ec86013bd&imgtype=0&src=http%3A%2F%2Ffile02.16sucai.com%2Fd%2Ffile%2F2015%2F0408%2F779334da99e40adb587d0ba715eca102.jpg", "link": "/"}
                ],
                "children": {
                    "women": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ],
                    "man": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ],
                    "material": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ]
                },
                "id": "cat-simple"
            },
            {
                "name": {
                    "en": "Street",
                    "zh_CN": "街头"
                },
                "banner": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589909869275&di=25ead44cab83131204f3b36ef9de513a&imgtype=0&src=http%3A%2F%2Fa2.att.hudong.com%2F36%2F48%2F19300001357258133412489354717.jpg", "link": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657341&di=e29b400824bb44c686795dd8531fa9a5&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F64%2F76%2F20300001349415131407760417677.jpg", "linke": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657436&di=b7d190c972effc30bc5f121ec86013bd&imgtype=0&src=http%3A%2F%2Ffile02.16sucai.com%2Fd%2Ffile%2F2015%2F0408%2F779334da99e40adb587d0ba715eca102.jpg", "link": "/"}
                ],
                "children": {
                    "women": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ],
                    "man": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ],
                    "material": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ]
                },
                "id": "111111"
            },
            {
                "name": {
                    "en": "Korea",
                    "zh_CN": "韩版"
                },
                "banner": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589909869275&di=25ead44cab83131204f3b36ef9de513a&imgtype=0&src=http%3A%2F%2Fa2.att.hudong.com%2F36%2F48%2F19300001357258133412489354717.jpg", "link": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657341&di=e29b400824bb44c686795dd8531fa9a5&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F64%2F76%2F20300001349415131407760417677.jpg", "linke": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657436&di=b7d190c972effc30bc5f121ec86013bd&imgtype=0&src=http%3A%2F%2Ffile02.16sucai.com%2Fd%2Ffile%2F2015%2F0408%2F779334da99e40adb587d0ba715eca102.jpg", "link": "/"}
                ],
                "children": {
                    "women": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ],
                    "man": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ],
                    "material": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ]
                },
                "id": "cat-korea"
            },
            {
                "name": {
                    "en": "Western",
                    "zh_CN": "欧美"
                },
                "banner": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589909869275&di=25ead44cab83131204f3b36ef9de513a&imgtype=0&src=http%3A%2F%2Fa2.att.hudong.com%2F36%2F48%2F19300001357258133412489354717.jpg", "link": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657341&di=e29b400824bb44c686795dd8531fa9a5&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F64%2F76%2F20300001349415131407760417677.jpg", "linke": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657436&di=b7d190c972effc30bc5f121ec86013bd&imgtype=0&src=http%3A%2F%2Ffile02.16sucai.com%2Fd%2Ffile%2F2015%2F0408%2F779334da99e40adb587d0ba715eca102.jpg", "link": "/"}
                ],
                "children": {
                    "women": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ],
                    "man": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ],
                    "material": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ]
                },
                "id": "cat-western"
            },
            {
                "name": {
                    "en": "Area",
                    "zh_CN": "地域"
                },
                "banner": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589909869275&di=25ead44cab83131204f3b36ef9de513a&imgtype=0&src=http%3A%2F%2Fa2.att.hudong.com%2F36%2F48%2F19300001357258133412489354717.jpg", "link": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657341&di=e29b400824bb44c686795dd8531fa9a5&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F64%2F76%2F20300001349415131407760417677.jpg", "linke": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657436&di=b7d190c972effc30bc5f121ec86013bd&imgtype=0&src=http%3A%2F%2Ffile02.16sucai.com%2Fd%2Ffile%2F2015%2F0408%2F779334da99e40adb587d0ba715eca102.jpg", "link": "/"}
                ],
                "children": {
                    "women": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ],
                    "man": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ],
                    "material": [
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                        {
                            "name": {
                                "en": "T-Shirt",
                                "zh_CN": "T恤"
                            },
                            "id": "cat-t-shirt",
                        },
                    ]
                },
                "id": "cat-area"
            },
        ],
        "total": 6
    }
}
@app.route('/v1/categories', methods=['GET'])
def get_categories():
    response = make_response(jsonify(categories))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response, 200

banners = {
    "code": 200,
    "data": {
        "items": [
            {"imageUrl": "http://image4.suning.cn/uimg/b2c/newcatentries/0070166958-000000000640627447_2_800x800.jpg", "link": "/"},
            {"imageUrl": "https://imgf1.pop-fashion.com/upload/flash_report/2020/2020051216/ANAREPORT_5eba616e80bde_2641.jpg", "link": "/"},
            {"imageUrl": "https://imgf2.pop-fashion.com/upload/flash_report/2020/2020040818/ANAREPORT_5e8da0d74d407_1568.jpg", "link": "/"},
            {"imageUrl": "https://imgf2.pop-fashion.com/upload/flash_report/2019/2019012617/ANAREPORT_5c4c27aa3a20f_3583.jpg", "link": "/"},
            {"imageUrl": "https://imgf3.pop-fashion.com/upload/flash_report/2020/2020032016/ANAREPORT_5e7479df81585_2517.jpg", "link": "/"}
        ],
        "total": 5
    }
}
@app.route('/v1/banners', methods=['GET'])
def get_banners():
    response = make_response(jsonify(banners))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response, 200

newIns = {
    "code": 200,
    "data": {
        "items": [
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850438080&di=3adf68cc1b6fc5de871b9fccb8f44c8f&imgtype=0&src=http%3A%2F%2Ft9.baidu.com%2Fit%2Fu%3D2266751744%2C4253267866%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D854",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850438080&di=11b88e68b2b1841e0db01dabeb75a7d3&imgtype=0&src=http%3A%2F%2Ft9.baidu.com%2Fit%2Fu%3D3949188917%2C63856583%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D875",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850786083&di=cb5861f92397729e580638d8409220e6&imgtype=0&src=http%3A%2F%2Fpic.90sjimg.com%2Fdesign%2F01%2F37%2F57%2F76%2F593572dcc604b.png",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850436548&di=5c8f95a0e7ebca520f00c223bda1a096&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D2857883419%2C1187496708%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D763",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850436544&di=9c1c91aabd8ede5b221d3e16dc9b3d50&imgtype=0&src=http%3A%2F%2Ft9.baidu.com%2Fit%2Fu%3D1577456063%2C1344044640%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850519963&di=7e9bee9dbcd0a1c93d803826ab30b081&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D2743642606%2C770505870%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D3816%26h%3D1960",
                "backImageUrl": "http://img0.imgtn.bdimg.com/it/u=3769023270,3433174748&fm=214&gp=0.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "http://00.minipic.eastday.com/20170503/20170503000024_d41d8cd98f00b204e9800998ecf8427e_7.jpeg",
                "backImageUrl": "http://img0.imgtn.bdimg.com/it/u=1125723489,855057867&fm=26&gp=0.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850647561&di=6c088359e808c2a58855b74751c9fcca&imgtype=0&src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farticle%2Fd8ec5e709b224bbdc9a804e3a3faeab8b24cb45b.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850647560&di=3fa6db518f935dc3e87a47fbd2a5bd88&imgtype=0&src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farticle%2F9edc8a7916768f964a03db94046bfbf446ddc450.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
        ],
        "total": 5
    }
}
@app.route('/v1/newIns', methods=['GET'])
def get_newIns():
    response = make_response(jsonify(newIns))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response, 200

hots = {
    "code": 200,
    "data": {
        "items": [
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850438080&di=3adf68cc1b6fc5de871b9fccb8f44c8f&imgtype=0&src=http%3A%2F%2Ft9.baidu.com%2Fit%2Fu%3D2266751744%2C4253267866%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D854",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850438080&di=11b88e68b2b1841e0db01dabeb75a7d3&imgtype=0&src=http%3A%2F%2Ft9.baidu.com%2Fit%2Fu%3D3949188917%2C63856583%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D875",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850786083&di=cb5861f92397729e580638d8409220e6&imgtype=0&src=http%3A%2F%2Fpic.90sjimg.com%2Fdesign%2F01%2F37%2F57%2F76%2F593572dcc604b.png",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ],
                "id": "1000000",
                "link": "/products/name"
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850436548&di=5c8f95a0e7ebca520f00c223bda1a096&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D2857883419%2C1187496708%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D763",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850436544&di=9c1c91aabd8ede5b221d3e16dc9b3d50&imgtype=0&src=http%3A%2F%2Ft9.baidu.com%2Fit%2Fu%3D1577456063%2C1344044640%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ],
                "id": "1000001",
                "link": "/products/name"
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850519963&di=7e9bee9dbcd0a1c93d803826ab30b081&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D2743642606%2C770505870%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D3816%26h%3D1960",
                "backImageUrl": "http://img0.imgtn.bdimg.com/it/u=3769023270,3433174748&fm=214&gp=0.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ],
                "id": "1000002",
                "link": "/products/name"
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "http://00.minipic.eastday.com/20170503/20170503000024_d41d8cd98f00b204e9800998ecf8427e_7.jpeg",
                "backImageUrl": "http://img0.imgtn.bdimg.com/it/u=1125723489,855057867&fm=26&gp=0.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ],
                "id": "1000003",
                "link": "/products/name"
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850647561&di=6c088359e808c2a58855b74751c9fcca&imgtype=0&src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farticle%2Fd8ec5e709b224bbdc9a804e3a3faeab8b24cb45b.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850647560&di=3fa6db518f935dc3e87a47fbd2a5bd88&imgtype=0&src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farticle%2F9edc8a7916768f964a03db94046bfbf446ddc450.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ],
                "id": "1000004",
                "link": "/products/name"
            },
        ],
        "total": 5
    }
}
@app.route('/v1/hots', methods=['GET'])
def get_hots():
    response = make_response(jsonify(hots))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response, 200

footers = {
    "code": 200,
    "data": {
        "items": [
            {
                "account": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/account", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/account/orders", "value": "orders"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/account/orders?q=return", "value": "return orders"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/account/orders?q=refund", "value": "refund orders"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/account/orders?q=shipping", "value": "shipping"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/carts", "value": "carts"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/checkout", "value": "checkout"}
                ]
            },
            {
                "Company": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/about", "value": "about"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/sitemap.xml", "value": "sitemap"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/robots.txt", "value": "robots"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/faq", "value": "Contact & FAQ"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/help", "value": "help"},
                ]
            },
            {
                "Connect": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "G-Mail"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "Twitter"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "Facebook"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "WeChat"},
                ]
            },
            {
                "policy": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/policy", "value": "Privacy Policy"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/terms", "value": "Terms of Service"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/policy/payments", "value": "Payments"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/policy/referral", "value": "Referral Program"},
                ]
            },
        ],
        "total": 5,
        "company": "SoftSun.com",
        "year": 2020,
    }
}
@app.route('/v1/footers', methods=['GET'])
def get_footers():
    response = make_response(jsonify(footers))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response, 200

carts = {
    "code": 200,
    "data": {
        "items": [
            {"value": "color,size", "count": 3, "link": "", "price": 11.9, "imageUrl": "//localhost:13147/images/67/18/2636167883511603206718.png"},
            {"value": "color,size", "count": 2, "link": "", "price": 8.9, "imageUrl": "//localhost:13147/images/67/18/2636167883511603206718.png"},
            {"value": "color,size", "count": 1, "link": "", "price": 5.9, "imageUrl": "//localhost:13147/images/67/18/2636167883511603206718.png"},
        ],
        "total": 3,
    },
}
@app.route('/v1/carts', methods=['GET'])
def get_carts():
    response = make_response(jsonify(carts))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response, 200

sizes = {
    "code": 200,
    "data": {
        "items": [
            { "value": "1111"},
            { "value": "12222"},
            { "value": "11111"},
            { "value": "1111"},
        ],
        "total": 3,
    },
}
@app.route('/v1/sizes', methods=['GET'])
def get_sizes():
    response = make_response(jsonify(sizes))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response, 200

colors = {
    "code": 200,
    "data": {
        "items": [
            {"name": "11", "value": "#100000"},
            {"name": "11", "value": "#100000"},
            {"name": "11", "value": "#101100"},
            {"name": "11", "value": "#100000"},
            {"name": "11", "value": "#100000"},
            {"name": "11", "value": "#100ff0"},
            {"name": "11", "value": "#100000"},
        ],
        "total": 5
    },
}
@app.route('/v1/colors', methods=['GET'])
def get_colors():
    response = make_response(jsonify(colors))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response, 200

goods = {
    "code": 200,
    "data": {
        "items": [
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
        ]
    }
}
@app.route('/v1/goods', methods=['GET'])
def get_goods():
    response = make_response(jsonify(goods))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response, 200

oneGoods={
    "code": 200,
    "data": {
        "name": {"en": "name"},
        "price": 123.5,
        "statePrice": 110,
        "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg",
        "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
        "state": 0,
        "nextState": 1,
        "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
        "colors": [
            {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
            {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
            {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
            {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
            {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
            {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
            {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
            {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
            {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
            {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
            {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
            {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
            {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
            {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
        ],
        "sizes": [
            "XSS", "XS", "S", "M", "L", "XL", "XLL"
        ],
        "thumbs": [
            {"imageUrl": "http://img1.pconline.com.cn/piclib/200811/17/batch/1/16797/1226885443432wk6gzq1nsd.jpg"},
            {"imageUrl": "http://attach.bbs.miui.com/forum/201105/17/113554rnu40q7nbgnn3lgq.jpg"},
            {"imageUrl": "http://attach.bbs.miui.com/forum/201311/17/174124tp3sa6vvckc25oc8.jpg"},
            {"imageUrl": "http://attach.bbs.miui.com/forum/201401/11/145825zn1sxa8anrg11gt1.jpg"},
            {"imageUrl": "http://11136604.s21i-11.faiusr.com/2/ABUIABACGAAgpLTDwwUol8ydmAQwgA84uAg.jpg"},
            {"imageUrl": "http://attachments.gfan.com/forum/201608/04/2339412b3z30zbd2j6k652.jpg"},
            {"imageUrl": "http://00.minipic.eastday.com/20170407/20170407003732_b667d194a4d001919e38b014cbe5ffb3_1.jpeg"},
            {"imageUrl": "http://attach.bbs.miui.com/forum/201204/17/1539083wxpexg5b0fbvzpv.jpg"},
            {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590840196499&di=2da215f27d5e2196b235194088e4c95f&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D747431361%2C2735836448%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D3682%26h%3D2457"},
            {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590840196499&di=88989e0f6c724affce44108c37d92524&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1223527042%2C3426233183%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D854"},
            {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590840196499&di=88989e0f6c724affce44108c37d92524&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1223527042%2C3426233183%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D854"},
            {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590840196498&di=d59a05e1e255160076a8d38bf316bf0a&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1535171809%2C1773958280%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D2296%26h%3D3440"},
            {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590840196498&di=3fc8dfe6244989bd0c5004ba9c25390d&imgtype=0&src=http%3A%2F%2Ft9.baidu.com%2Fit%2Fu%3D932647289%2C4139427096%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D854"},
        ],
        "desc": [
            {"group": [
                {"value": "商家对商品材质、成份等信息的描", "link": "/"},
                {"value": "七天无理由退货", "link": "/"},
                {"value": "保质期", "link": "/"},
                {"value": "材质", "link": "/"},
                {"value": "联系客服", "link": "/"},
                {"value": "保质期", "link": "/"},
            ]},
            {"group": [
                {"value": "11111", "link": "/"},
                {"value": "11111", "link": "/"},
                {"value": "11111", "link": "/"},
            ]},
            {"group": [
                {"value": "分期付款", "link": "/"},
                {"value": "支付宝", "link": "/"},
                {"value": "微信", "link": "/"},
                {"value": "信用卡", "link": "/"},
            ]},
        ]
    }
}
@app.route('/v1/goods/', methods=['GET'])
def get_one_goods():
    response = make_response(jsonify(oneGoods))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response, 200

similar = {
    "code": 200,
    "data": {
        "items": [
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850438080&di=3adf68cc1b6fc5de871b9fccb8f44c8f&imgtype=0&src=http%3A%2F%2Ft9.baidu.com%2Fit%2Fu%3D2266751744%2C4253267866%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D854",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850438080&di=11b88e68b2b1841e0db01dabeb75a7d3&imgtype=0&src=http%3A%2F%2Ft9.baidu.com%2Fit%2Fu%3D3949188917%2C63856583%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D875",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850786083&di=cb5861f92397729e580638d8409220e6&imgtype=0&src=http%3A%2F%2Fpic.90sjimg.com%2Fdesign%2F01%2F37%2F57%2F76%2F593572dcc604b.png",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850436548&di=5c8f95a0e7ebca520f00c223bda1a096&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D2857883419%2C1187496708%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D763",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850436544&di=9c1c91aabd8ede5b221d3e16dc9b3d50&imgtype=0&src=http%3A%2F%2Ft9.baidu.com%2Fit%2Fu%3D1577456063%2C1344044640%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850519963&di=7e9bee9dbcd0a1c93d803826ab30b081&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D2743642606%2C770505870%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D3816%26h%3D1960",
                "backImageUrl": "http://img0.imgtn.bdimg.com/it/u=3769023270,3433174748&fm=214&gp=0.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "http://00.minipic.eastday.com/20170503/20170503000024_d41d8cd98f00b204e9800998ecf8427e_7.jpeg",
                "backImageUrl": "http://img0.imgtn.bdimg.com/it/u=1125723489,855057867&fm=26&gp=0.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
            {
                "name": {"en": "name"},
                "price": 123.5,
                "statePrice": 110,
                "imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850647561&di=6c088359e808c2a58855b74751c9fcca&imgtype=0&src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farticle%2Fd8ec5e709b224bbdc9a804e3a3faeab8b24cb45b.jpg",
                "backImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590850647560&di=3fa6db518f935dc3e87a47fbd2a5bd88&imgtype=0&src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farticle%2F9edc8a7916768f964a03db94046bfbf446ddc450.jpg",
                "state": 0,
                "nextState": 1,
                "stateImageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                "colors": [
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ff0000"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#ffff00"},
                    {"name": {"en": "en", "zh_CN": "zh_CN"}, "rgb": "#aabbcc"},
                ],
                "sizes": [
                    "XSS", "XS", "S", "M", "L", "XL", "XLL"
                ]
            },
        ]
    }
}
@app.route('/v1/similarGoods/', methods=['GET'])
def get_similar_goods():
    response = make_response(jsonify(similar))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response, 200

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 20520,
        debug = True
        )
