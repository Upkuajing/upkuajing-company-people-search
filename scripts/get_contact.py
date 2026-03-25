#!/usr/bin/env python3
"""
跨境魔方联系方式
获取公司或人物的联系方式（邮箱、电话、社交媒体、网站）。
"""
import argparse
import sys
from common import make_request, print_json_output


def get_contact(bus_id: str, bus_type: int) -> dict:
    """
    获取公司或人物的联系方式。

    Args:
        bus_id: 业务ID（公司ID或人物ID）
        bus_type: 业务类型（1=公司，2=人物）

    Returns:
        包含联系方式的API响应
    """
    params = {
        'bus_id': bus_id,
        'bus_type': bus_type
    }
    response = make_request('/search/contact', params)
    return response


def main():
    parser = argparse.ArgumentParser(
        description='从跨境魔方开放平台获取联系方式'
    )
    parser.add_argument(
        '--bus_id',
        required=True,
        help='公司ID或人物ID'
    )
    parser.add_argument(
        '--bus_type',
        type=int,
        required=True,
        choices=[1, 2],
        help='业务类型：1=公司，2=人物'
    )

    args = parser.parse_args()

    # 获取联系方式
    response = get_contact(args.bus_id, args.bus_type)

    # 从响应中提取数据
    if response.get('code') == 0:
        data = response.get('data', {})
        # 提取费用信息 金额单位 分钱
        api_cost = response.get('fee', {}).get("apiCost", 0)
        print_json_output({"data": data, "apiCost": f"{api_cost}分钱"})
    else:
        print(f"错误：{response.get('msg', '未知错误')}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
