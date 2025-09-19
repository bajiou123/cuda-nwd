import json


def main(arg):
    # 如果输入是字符串，则解析为字典
    if isinstance(arg, str):
        try:
            data = json.loads(arg)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON string provided"}
    else:
        data = arg

    results = []

    # 检查是否存在result字段且是否为列表
    if "arg" not in data or not isinstance(data["arg"], list):
        return {"error": "Expected 'arg' field to be an array"}

    # 遍历所有分段
    for item in data["arg"]:
        # 确保每个分段都有metadata
        metadata = item.get("metadata", {})
        dataset_name = metadata.get("dataset_name", "Unknown Dataset")
        document_name = metadata.get("document_name", "Unknown Document")
        score = metadata.get("score", 0)

        # 拼接字符串
        concatenated_str = f"{dataset_name}，{document_name}，{score}"
        results.append(concatenated_str)

    return results

def main(arg1: str) -> dict:
    return {
        "result": arg1
    }

if __name__ == "__main__":
    # 你的数据样例（这里用你之前提供的例子）
    example_input = {
  "arg": [
    {
      "metadata": {
        "_source": "knowledge",
        "dataset_id": "8d4c3161-52d7-4b32-a187-2a9ba3f1318f",
        "dataset_name": "惠州市惠城区-区县公共服务事项清单",
        "document_id": "f34f8cd1-5f9d-415f-a88d-6f28c1025c8c",
        "document_name": "惠城区_失业保险金申领_1244130045.docx",
        "document_data_source_type": "upload_file",
        "segment_id": "92e96273-9882-480d-b69b-af0b67a93f91",
        "retriever_from": "workflow",
        "score": 0.74461377,
        "segment_hit_count": 7,
        "segment_word_count": 24,
        "segment_position": 29,
        "segment_index_node_hash": "cc06add242a5117e62f89960cc94072ba19b589bc154b44b1d98193992a0643a",
        "doc_metadata": None,
        "position": 1
      },
      "title": "惠城区_失业保险金申领_1244130045.docx",
      "content": "失业前用人单位和本人已经缴纳失业保险费满一年的；"
    },
    {
      "metadata": {
        "_source": "knowledge",
        "dataset_id": "8d4c3161-52d7-4b32-a187-2a9ba3f1318f",
        "dataset_name": "惠州市惠城区-区县公共服务事项清单",
        "document_id": "f34f8cd1-5f9d-415f-a88d-6f28c1025c8c",
        "document_name": "惠城区_失业保险金申领_1244130045.docx",
        "document_data_source_type": "upload_file",
        "segment_id": "ef63549c-55df-4cbd-8645-90a33b17bbf1",
        "retriever_from": "workflow",
        "score": 0.7250402,
        "segment_hit_count": 7,
        "segment_word_count": 46,
        "segment_position": 3,
        "segment_index_node_hash": "55cf761edbfb842128e70ef2fcf6bdca9fa5be4c2a7e5781a1a7acf105c7dbcc",
        "doc_metadata": None,
        "position": 2
      },
      "title": "惠城区_失业保险金申领_1244130045.docx",
      "content": "失业前用人单位和本人已经缴纳失业保险费累计满一年，或者不满一年但本人有失业保险金领取期限的；"
    },
    {
      "metadata": {
        "_source": "knowledge",
        "dataset_id": "a34e4dd3-18c8-4f3c-bdd9-6b57f6e49a8d",
        "dataset_name": "数字人知识库4",
        "document_id": "d79138f2-60ff-4691-904f-6e9c9bbff3c9",
        "document_name": "政策法规_政策解读_《广东省人力资源和社会保障厅 广东省财政厅 国家税务总局广东省税务局关于做好失业保险稳岗位提技能防失业工作的通知》政策解读.docx",
        "document_data_source_type": "upload_file",
        "segment_id": "d4888dc5-41a2-41ea-b57b-256b9e7134ef",
        "retriever_from": "workflow",
        "score": 0.69604087,
        "segment_hit_count": 21,
        "segment_word_count": 143,
        "segment_position": 30,
        "segment_index_node_hash": "a3fc735403a69d7bb093885fb447cf5563f4e0731e16099a91cf1e63610fb1ad",
        "doc_metadata": None,
        "position": 3
      },
      "title": "政策法规_政策解读_《广东省人力资源和社会保障厅 广东省财政厅 国家税务总局广东省税务局关于做好失业保险稳岗位提技能防失业工作的通知》政策解读.docx",
      "content": "根据《广东省失业保险条例》第十五条规定，失业人员同时符合下列条件的，可以领取失业保险金，并按照规定享受其他失业保险待遇：（一）失业前用人单位和本人已经缴纳失业保险费累计满一年，或者不满一年但本人有失业保险金领取期限的；（二）非因本人意愿中断就业的；（三）已经办理失业登记，并有求职要求的"
    },
    {
      "metadata": {
        "_source": "knowledge",
        "dataset_id": "be948c45-707e-4f43-8941-ac8409508275",
        "dataset_name": "数字人知识库0503简版",
        "document_id": "bf035f1f-50cd-4ccf-8a28-c0a75e27f999",
        "document_name": "人力资源社会保障部办公厅 财政部办公厅 国家税务总局办公厅 国家医保局办公室关于进一步提升失业保险经办服务质效的通知.docx",
        "document_data_source_type": "upload_file",
        "segment_id": "d53e43b4-0d82-4526-bb30-f80f4e883993",
        "retriever_from": "workflow",
        "score": 0.68469143,
        "segment_hit_count": 10,
        "segment_word_count": 185,
        "segment_position": 6,
        "segment_index_node_hash": "133dfb71b7e94952ca011495017bfa153329651df972daee21499b448bad83dd",
        "doc_metadata": None,
        "position": 4
      },
      "title": "人力资源社会保障部办公厅 财政部办公厅 国家税务总局办公厅 国家医保局办公室关于进一步提升失业保险经办服务质效的通知.docx",
      "content": "失业人员因用人单位认定停保原因为本人意愿主动离职而无法申领失业保险金的，如其本人提出申请并能证明非因本人意愿中断就业，经办机构应据实重新核实认定，符合条件的发放失业保险金\n六、加强证书审核参保企业职工或领取失业保险金人员持证申请失业保险技能提升补贴的，经办机构要通过职业资格证书或职业技能等级证书联网查询方式进行审核，要确保证岗相适，相关证书应在技能人才评价工作网可查询"
    }
  ]
}

    processed_results = main(example_input)
    for result in processed_results:
        print(result)