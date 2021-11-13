import os


from flask import Flask,jsonify,request
import json


app = Flask(__name__,static_url_path='/static')

base_dir = os.path.realpath(os.path.dirname(__file__))

def get_json(filename):
    data = json.load(open(os.path.join(base_dir,filename),'r'))
    return data

@app.route('/', methods=['GET'])
def test():
    return jsonify(get_json("test.json"))


@app.route('/api/channel/enterprise-user/getTotalRate', methods=['GET', 'POST'])
def home_summary():
    return jsonify(get_json("home_summary.json"))

@app.route('/api/channel/hospital/getStatistics', methods=['GET', 'POST'])
def home_summary2():
    return jsonify(get_json("home_summary2.json"))

@app.route('/api/user/questionnaire-user-question/getHealthRate', methods=['GET', 'POST'])
def getHealthRate():
    return jsonify(get_json("question_health_rate.json"))

@app.route('/api/user/user-info/getUserInfoRate', methods=['GET', 'POST'])
def getUserInfoRate():
    return jsonify(get_json("userinfo_rate.json"))

@app.route('/api/channel/enterprise/getIndustryRate', methods=['GET', 'POST'])
def getIndustryRate():
    return jsonify(get_json("getIndustryRate.json"))

# @app.route('/api/channel/enterprise/getSignUp', methods=['GET', 'POST'])
# def signUp():
#      return jsonify(get_json("sign_up.json"))


@app.route('/api/channel/hospital/getQuarterly', methods=['GET', 'POST'])
def getQuarterly():
     return jsonify(get_json("quarterly.json"))


@app.route('/api/channel/enterprise/getArea', methods=['GET', 'POST'])
def get_area():
    return jsonify(get_json("area.json"))

@app.route('/api/user/hospital-comment/getHospitalPraiseRate', methods=['GET', 'POST'])
def getHospitalPraiseRate():
    return jsonify(get_json("getHospitalPraiseRate.json"))

@app.route('/api/order/user-order/getPhysicalExamination', methods=['GET', 'POST'])
def getPhysicalExamination():
    return jsonify(get_json("getPhysicalExamination.json"))


@app.route('/api/order/user-order/getArrivalRate', methods=['GET', 'POST'])
def getArrivalRate():
    return jsonify(get_json("getArrivalRate.json"))


@app.route('/api/order/user-order/getTopHospitalCityRate', methods=['GET', 'POST'])
def getTopHospitalCityRate():
    type = request.args.get("type")
    if type == 1:
        return jsonify(get_json("getArrivalRate.json"))
    else:
        return jsonify(get_json("provinceData.json"))


@app.route('/api/order/user-order/getCityCountByProvince', methods=['GET', 'POST'])
def getCityCountByProvince():
    return jsonify(get_json("getCityCountByProvince.json"))


@app.route('/api/businessdomain/common-test-result/fetchTestItemTotal', methods=['GET', 'POST'])
def fetchTestItemTotal():
    return jsonify(get_json("fetchTestItemTotal.json"))


# @app.route('/api/channel/hospital/getArea', methods=['GET', 'POST'])
# def getArea():
#     return jsonify(get_json("getArea.json"))

@app.route('/api/channel/hospital/getSignUp', methods=['GET', 'POST'])
def getSignUp():
    return jsonify(get_json("getSignUp.json"))


@app.route('/api/channel/enterprise/getSignUp', methods=['GET', 'POST'])
def getEnterpriseSignUp():
    return jsonify(get_json("enterpriseGetSignUp.json"))


@app.route('/api/channel/hospital/getArea', methods=['GET', 'POST'])
def getTotalArea():
    return jsonify(get_json("total_area.json"))