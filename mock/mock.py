# /usr/bin/env python
# -*- coding:utf-8 -*-

# pip install flask
from flask import abort, jsonify, Flask, request, Response, make_response

app = Flask(__name__)
# 增加配置，支持中文显示
app.config['JSON_AS_ASCII'] = False

notices = {
    "code": 200,
    "data": {
        "items": [
            {
                "value": "111444中国你好111444中国你好",
                "link": "/",
                "icon": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg"
            },
            {
                "value": "222",
                "icon": ""
            },
            {
                "value": "333",
                "icon": ""
            },
            {
                "value": "444中国你好",
                "link": "/",
                "icon": ""
            }
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

countries = {
    "code": 200,
    "data": {
        "items": [
            {
                "key": "en",
                "value": "US"
            },
            {
                "key": "zh_CN",
                "value": "China"
            }
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


categories = {
    "code": 200,
    "data": {
        "items": [
            {
                "name": {
                    "en": "1111",
                    "zh_CN": "一一一"
                },
                "banner": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589909869275&di=25ead44cab83131204f3b36ef9de513a&imgtype=0&src=http%3A%2F%2Fa2.att.hudong.com%2F36%2F48%2F19300001357258133412489354717.jpg", "link": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657341&di=e29b400824bb44c686795dd8531fa9a5&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F64%2F76%2F20300001349415131407760417677.jpg", "linke": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657436&di=b7d190c972effc30bc5f121ec86013bd&imgtype=0&src=http%3A%2F%2Ffile02.16sucai.com%2Fd%2Ffile%2F2015%2F0408%2F779334da99e40adb587d0ba715eca102.jpg", "link": "/"}
                ],
                "children": [
                    {"name": {"en": "11"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222}
                ],
                "id": "111111"
            },
            {
                "name": {
                    "en": "1111",
                    "zh_CN": "一一一"
                },
                "banner": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589909869275&di=25ead44cab83131204f3b36ef9de513a&imgtype=0&src=http%3A%2F%2Fa2.att.hudong.com%2F36%2F48%2F19300001357258133412489354717.jpg", "link": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657341&di=e29b400824bb44c686795dd8531fa9a5&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F64%2F76%2F20300001349415131407760417677.jpg", "linke": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657436&di=b7d190c972effc30bc5f121ec86013bd&imgtype=0&src=http%3A%2F%2Ffile02.16sucai.com%2Fd%2Ffile%2F2015%2F0408%2F779334da99e40adb587d0ba715eca102.jpg", "link": "/"}
                ],
                "children": [
                    {"name": {"en": "11"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222}
                ],
                "id": "111111"
            },
            {
                "name": {
                    "en": "1111",
                    "zh_CN": "一一一"
                },
                "banner": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589909869275&di=25ead44cab83131204f3b36ef9de513a&imgtype=0&src=http%3A%2F%2Fa2.att.hudong.com%2F36%2F48%2F19300001357258133412489354717.jpg", "link": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657341&di=e29b400824bb44c686795dd8531fa9a5&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F64%2F76%2F20300001349415131407760417677.jpg", "linke": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657436&di=b7d190c972effc30bc5f121ec86013bd&imgtype=0&src=http%3A%2F%2Ffile02.16sucai.com%2Fd%2Ffile%2F2015%2F0408%2F779334da99e40adb587d0ba715eca102.jpg", "link": "/"}
                ],
                "children": [
                    {"name": {"en": "11"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222}
                ],
                "id": "111111"
            },
            {
                "name": {
                    "en": "1111",
                    "zh_CN": "一一一"
                },
                "banner": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589909869275&di=25ead44cab83131204f3b36ef9de513a&imgtype=0&src=http%3A%2F%2Fa2.att.hudong.com%2F36%2F48%2F19300001357258133412489354717.jpg", "link": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657341&di=e29b400824bb44c686795dd8531fa9a5&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F64%2F76%2F20300001349415131407760417677.jpg", "linke": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657436&di=b7d190c972effc30bc5f121ec86013bd&imgtype=0&src=http%3A%2F%2Ffile02.16sucai.com%2Fd%2Ffile%2F2015%2F0408%2F779334da99e40adb587d0ba715eca102.jpg", "link": "/"}
                ],
                "children": [
                    {"name": {"en": "11"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222}
                ],
                "id": "111111"
            },
            {
                "name": {
                    "en": "1111",
                    "zh_CN": "一一一"
                },
                "banner": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589909869275&di=25ead44cab83131204f3b36ef9de513a&imgtype=0&src=http%3A%2F%2Fa2.att.hudong.com%2F36%2F48%2F19300001357258133412489354717.jpg", "link": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657341&di=e29b400824bb44c686795dd8531fa9a5&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F64%2F76%2F20300001349415131407760417677.jpg", "linke": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657436&di=b7d190c972effc30bc5f121ec86013bd&imgtype=0&src=http%3A%2F%2Ffile02.16sucai.com%2Fd%2Ffile%2F2015%2F0408%2F779334da99e40adb587d0ba715eca102.jpg", "link": "/"}
                ],
                "children": [
                    {"name": {"en": "11"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222}
                ],
                "id": "111111"
            },
            {
                "name": {
                    "en": "1111",
                    "zh_CN": "一一一"
                },
                "banner": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589909869275&di=25ead44cab83131204f3b36ef9de513a&imgtype=0&src=http%3A%2F%2Fa2.att.hudong.com%2F36%2F48%2F19300001357258133412489354717.jpg", "link": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657341&di=e29b400824bb44c686795dd8531fa9a5&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F64%2F76%2F20300001349415131407760417677.jpg", "linke": "/"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589910657436&di=b7d190c972effc30bc5f121ec86013bd&imgtype=0&src=http%3A%2F%2Ffile02.16sucai.com%2Fd%2Ffile%2F2015%2F0408%2F779334da99e40adb587d0ba715eca102.jpg", "link": "/"}
                ],
                "children": [
                    {"name": {"en": "11"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222},
                    {"name": {"en": "111"}, "id": 1111222}
                ],
                "id": "111111"
            }
        ],
        "total": 2
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
            {"imageUrl": "http://pic1.nipic.com/2009-02-18/200921881948663_2.jpg", "link": "/"},
            {"imageUrl": "http://image.biaobaiju.com/uploads/20190825/15/1566716852-ZaGILPRHMC.jpg", "link": "/"},
            {"imageUrl": "http://piccdn.sharer.com.tw/_myshareupload/member/681/121911114945508.jpg", "link": "/"},
            {"imageUrl": "http://pic15.nipic.com/20110811/7561713_113238460157_2.jpg", "link": "/"},
            {"imageUrl": "http://image.biaobaiju.com/uploads/20180918/18/1537267738-bWIZqVYARd.jpg", "link": "/"}
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
            {"imageUrl": "http://image.biaobaiju.com/uploads/20180918/18/1537267738-bWIZqVYARd.jpg", "link": "/"},
            {"imageUrl": "http://img.zx123.cn/Resources/zx123cn/uploadfile/2015/1103/20151103101413_45817.jpg", "link": "/"},
            {"imageUrl": "http://gss0.baidu.com/94o3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/b58f8c5494eef01f0a7349cbe1fe9925bc317d5c.jpg", "link": "/"},
            {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590169948470&di=21ab6ec6354e4d5dabed6e1a1eb698b1&imgtype=0&src=http%3A%2F%2Fa3.att.hudong.com%2F14%2F75%2F01300000164186121366756803686.jpg", "link": "/"},
            {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590169948470&di=e8f7f7805b3635fb2421f45a63284028&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F64%2F76%2F20300001349415131407760417677.jpg", "link": "/"},
            {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590169948470&di=4337e57b0485955e9a94e6a402de1651&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F56%2F12%2F01300000164151121576126282411.jpg", "link": "/"}
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
            {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/"},
            {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=0ffeb0582709c9b0474c95290293edf5&imgtype=0&src=http%3A%2F%2Ft9.baidu.com%2Fit%2Fu%3D3363001160%2C1163944807%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D830", "link": "/"},
            {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=cb0cc70b7a21757a4ba5c19aea1a2132&imgtype=0&src=http%3A%2F%2Ft9.baidu.com%2Fit%2Fu%3D583874135%2C70653437%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D3607%26h%3D2408", "link": "/"},
            {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=52ec51d2a8bcb3862378a472852aa20d&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D2247852322%2C986532796%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/"},
            {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=bc76c350fdda29c2aa03b50819fa0c2b&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D3204887199%2C3790688592%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D4610%26h%3D2968", "link": "/"},
            {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=0ffeb0582709c9b0474c95290293edf5&imgtype=0&src=http%3A%2F%2Ft9.baidu.com%2Fit%2Fu%3D3363001160%2C1163944807%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D830", "link": "/"},
            {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612112&di=d2813c6168be4dedbf1e42a61846a311&imgtype=0&src=http%3A%2F%2Ft9.baidu.com%2Fit%2Fu%3D2268908537%2C2815455140%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D719", "link": "/"}
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
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                ]
            },
            {
                "link": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                ]
            },
            {
                "social": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                ]
            },
            {
                "policy": [
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
                    {"imageUrl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590219612113&di=405b784b41a0babea0afd3a05419c9f0&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853", "link": "/", "value": "account"},
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
