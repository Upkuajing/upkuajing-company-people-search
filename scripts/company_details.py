#!/usr/bin/env python3
"""
跨境魔方公司详情
获取公司的详细信息（工商信息）。
"""
import argparse
import sys
from common import make_request, print_json_output


def get_company_details(pid: str) -> dict:
    """
    根据公司ID获取公司详情。

    Args:
        pid: 公司ID（字符串）

    Returns:
        包含公司详情的API响应
    """
    params = {'pid': pid}
    response = make_request('/search/company/info', params)
    return response


def main():
    parser = argparse.ArgumentParser(
        description='从跨境魔方开放平台获取公司详情'
    )
    parser.add_argument(
        '--pid',
        required=True,
        help='公司ID'
    )

    args = parser.parse_args()

    # 获取公司详情
    response = get_company_details(args.pid)

    # 从响应中提取数据
    if response.get('code') == 0:
        data = response.get('data', {})
        print_json_output(data)
    else:
        print(f"错误：{response.get('msg', '未知错误')}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
