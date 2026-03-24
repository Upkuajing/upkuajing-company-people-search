#!/usr/bin/env python3
"""
跨境魔方人物详情
获取人物的详细信息。
"""
import argparse
import sys
from common import make_request, print_json_output


def get_human_details(hid: str) -> dict:
    """
    根据人物ID获取人物详情。

    Args:
        hid: 人物ID（字符串）

    Returns:
        包含人物详情的API响应
    """
    params = {'hid': hid}
    response = make_request('/search/person/info', params)
    return response


def main():
    parser = argparse.ArgumentParser(
        description='从跨境魔方开放平台获取人物详情'
    )
    parser.add_argument(
        '--hid',
        required=True,
        help='人物ID'
    )

    args = parser.parse_args()

    # 获取人物详情
    response = get_human_details(args.hid)

    # 从响应中提取数据
    if response.get('code') == 0:
        data = response.get('data', {})
        print_json_output(data)
    else:
        print(f"错误：{response.get('msg', '未知错误')}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
