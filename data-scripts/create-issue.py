import os
import json
from github import Github
import ciqreviews as ciq
from datetime import datetime

TOKEN = os.environ['GITHUB_TOKEN']
g = Github(TOKEN)
repo = g.get_repo(os.environ['OWNER'] + '/' + os.environ['REPO_NAME'])

# 2 kinds of issues
# 1. all developers' id-app dict
# 2. rolling download info for single developer from #1 issue
issues = repo.get_issues(q="ALL_DEVELOPER_APPS")

if len(issues) < 1:
    issue = repo.create_issue(
        "ALL_DEVELOPER_APPS", "{}")

else:
    issue = issues[0]
    comments = issue.get_comments()
    # dict: developerid - issue comment number
    # issue_body_dict = json.loads(issue.body)

    for comment in comments:
        # {
        #  udpate_at: ''
        #  developer_id : '',
        #  developer_name: '',
        #  developer_total: '',
        #  developer_total_cn: '',
        #  developer_total_row: '',
        #  apps:{
        #   'app_id':{
        #       'total_reviews_cn':2222,
        #       'total_reviews_row':2222,

        #       'average_rating_cn':3.4,
        #       'average_rating_row':4.7,

        #       'downloads_cn':2222,
        #       'app_name_row': '',
        #       'app_name_cn': '',
        #       'downloads_row':1111,
        #       'downloads_total':3333
        #   }
        #  }
        # }
        developer_dict = json.loads(comment.body)
        developer_id = developer_dict['developer_id']

        developer_name_row, total_download_row, app_dict_row = ciq.get_user_app_download_info(
            developer_id, 'row')
        developer_name_cn, download_cn, app_dict_cn = ciq.get_user_app_download_info(
            developer_id, 'cn')
        today_date = datetime.now().strftime("%Y_%m_%d")
        developer_dict['update_at'] = today_date
        developer_dict['developer_name'] = developer_name_row
        developer_dict['developer_total_cn'] = download_cn
        developer_dict['developer_total_row'] = download_row
        developer_dict['developer_total'] = int(
            download_row) + int(download_cn)

        for appid in app_dict_row.keys():
            if developer_dict['apps'][appid] is None:
                developer_dict['apps'][appid] = {}
            developer_dict['apps'][appid]['total_reviews_row'] = app_dict_row[appid]['total_reviews']
            developer_dict['apps'][appid]['average_rating_row'] = app_dict_row[appid]['average_rating']
            developer_dict['apps'][appid]['downloads_row'] = app_dict_row[appid]['total_downloads']
            developer_dict['apps'][appid]['app_name_row'] = app_dict_row[appid]['app_name']

            developer_dict['apps'][appid]['total_reviews_cn'] = app_dict_cn[appid]['total_reviews']
            developer_dict['apps'][appid]['average_rating_cn'] = app_dict_cn[appid]['average_rating']
            developer_dict['apps'][appid]['downloads_cn'] = app_dict_cn[appid]['total_downloads']
            developer_dict['apps'][appid]['app_name_cn'] = app_dict_cn[appid]['app_name']

        # issue.create_comment("<your-comment>")
        developer_dict_str = json.dumps(developer_dict)
        comment.edit(body=developer_dict_str)
