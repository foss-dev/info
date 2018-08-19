from flask import Flask, jsonify, request

from modules import (
    m_dns, m_port, m_admin_finder, m_site,
    m_cve, m_ip, m_pwned, m_password, m_ip_block_scanner,
    m_myBBPluginScanner
)

from util import u_domain

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/dns', methods=['POST'])
def dns_query():
    data = {}
    try:
        domain = u_domain.domain_resolve(request.form['domain'])

        data = m_dns.dns_records(domain)
    except:
        data = {}

    return jsonify(data)

@app.route('/port', methods=['POST'])
def port_query():
    domain = u_domain.domain_resolve(request.form['domain'])
    port = request.form["port"]

    data = m_port.check_port(domain, port)

    return jsonify(data)

@app.route('/find_admin', methods=['POST'])
def admin_query():
    domain = u_domain.domain_resolve(request.form['domain'])

    data = m_admin_finder.find_admin(domain)

    return jsonify(data)

@app.route('/site_info', methods=['POST'])
def site_info():
    domain = u_domain.domain_resolve(request.form['domain'])

    data = m_site.info(domain)

    return jsonify(data)

@app.route('/cve', methods=['POST'])
def cve_query():
    keyword = request.form["keyword"]

    data = m_cve.cve_result(keyword)

    return jsonify(data)

@app.route('/ip', methods=['POST'])
def ip_query():

    data = m_ip.get_ip(request)

    return jsonify(data)

@app.route('/pwned', methods=['POST'])
def pwned_query():

    try:
        query_type = request.form["type"]
    except:
        query_type = "have_i_been_pwned"


    keyword = request.form["keyword"]

    data = m_pwned.pwned(query_type, keyword)

    return jsonify(data)

@app.route('/password', methods=['POST'])
def password_generate():

    data = {}

    try:
        length = int(request.form["length"])
    except:
        length = 16

    posts = {
        "lower": request.form["lower"],
        "upper": request.form["upper"],
        "numeric": request.form["numeric"],
        "other": request.form["other"],
        "all": request.form["all"]
    }

    data["password"] = m_password.generate(posts, length)

    return jsonify(data)

@app.route('/ip_block', methods=['POST'])
def ip_block():
    ip = request.form["ip"]
    minimum = request.form["min"]
    maximum = request.form["max"]
    data = {}

    if int(minimum) < 0 or int(maximum) > 32:
        data = {
            "error": "IP Network Format. Range format must be in 0/32"
        }
    else:
        data = m_ip_block_scanner.scan(ip, minimum, maximum)

    return jsonify(data)

@app.route('/mybbPluginScanner', methods=['POST'])
def mybbPluginScanner():
    domain = u_domain.domain_resolve(request.form['domain'])

    data = m_myBBPluginScanner.pluginScanner(domain)

    return jsonify(data)

if __name__ == '__main__':
    app.run()
