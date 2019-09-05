import configparser
import csv
import sys

# read conf file and store into dictionary
config = configparser.RawConfigParser()
conf = config.read(sys.argv[1])
# Save all properties from all sections
sectionName = []
headers = []
values = []

for section in config.sections():
    # print("[" + section + "]")
    sectionName.append(section)
    for property in config[section]:
        # print(property + " = " + config[section][property])
        headers.append(property)
        values.append(config[section][property])


# print("**********DEBUG**********")
# print("There are a total of", len(headers), "headers extracted:")
# # print(headers)
# print("Here are the respective values:")
# for key in range(len(headers)):
#     print(headers[key], ": ", values[key])

# for elements in range(len(sys.argv)):
#     print(elements, ": ", sys.argv[elements])

# print(sys.argv[1])
# print(sys.argv[2:13])
# print("**********End of DEBUG**********")

# Generate section dictionary
propertyDic = dict(zip(headers, values))

# configure fieldnames
# temp fieldnames
# fieldNames = [action.correlationsearch.enabled", "action.correlationsearch.label", "action.customsearchbuilder.enabled", "action.customsearchbuilder.spec", "action.email", "action.email.to", "action.notable.param.verbose", "alert.suppress, "alert.track", "counttype", "cron_schedule", "description", "disabled", "dispatch.earliest_time", "dispatch.latest_time", "dispatch.rt_backfill", "enablesched", "quantity", "relation", "request.ui_dispatch_app", "search", "action.email.include.results_link", "action.email.include.view_link", "action.email.message.alert", "action.email.subject", "action.keyindicator.invert", "action.makestreams.param.verbose", "action.nbtstat.param.verbose", "action.notable", "action.notable.param.drilldown_name", "action.notable.param.drilldown_search", "action.notable.param.extract_assets", "action.notable.param.extract_identities", "action.notable.param.rule_description", "action.notable.param.rule_title", "action.notable.param.security_domain", "action.notable.param.severity", "action.nslookup.param.verbose", "action.ping.param.verbose", "action.risk", "action.risk.param._risk_object", "action.risk.param._risk_object_type", "action.risk.param._risk_score", "action.risk.param.verbose", "action.send2uba.param.verbose", "action.threat_add.param.verbose", "alert.suppress.fields", "alert.suppress.period"]

with open('../result.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    fieldnames = reader.fieldnames

# print(fieldnames)
# append csv with
with open('../result.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow(propertyDic)
