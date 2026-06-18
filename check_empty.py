def check_empty_label(label_text):
    """检查标注文本是否为空"""
    if not label_text or label_text.strip() == "":
        return True  # 是问题数据
    return False

# 简单测试
print(check_empty_label(""))      # 应输出 True
print(check_empty_label("正常"))  # 应输出 False