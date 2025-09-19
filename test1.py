import json
import string


def main(arg1: string, arg2: string, user_id: string, product_id: int, review: string) -> dict:
    mail_to = "kb_zhangsan123@163.com"
    title = "邮件标题"
    message = "邮件内容"
    d = {
        "mail_to": mail_to,
        "title": title,
        "message": message
    }
    return {
        "result": json.dumps(d, ensure_ascii=False)
    }
