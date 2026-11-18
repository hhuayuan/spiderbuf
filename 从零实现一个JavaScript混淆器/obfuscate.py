# 文章链接：https://spiderbuf.cn/article/javascript-obfuscator-ast-reverse-engineering
import esprima
import escodegen
import json
import secrets

# 保存函数名及变量名映射，保证声明和引用一致
name_map = {}

def random_hex():
    """生成随机十六进制标识符"""
    return "_0x" + secrets.token_hex(4)


def get_name(name):
    if name not in name_map:
        name_map[name] = random_hex()
    return name_map[name]

def traverse(node):
    if isinstance(node, dict):
        # 修改函数声明名称
        if node.get("type") == "FunctionDeclaration":
            if node.get("id"):
                node["id"]["name"] = get_name(
                    node["id"]["name"]
                )

        # 修改变量声明名称
        elif node.get("type") == "VariableDeclarator":
            if node.get("id", {}).get("type") == "Identifier":
                node["id"]["name"] = get_name(
                    node["id"]["name"]
                )

        # 修改标识符引用
        elif node.get("type") == "Identifier":
            name = node.get("name")

            if name in name_map:
                node["name"] = name_map[name]

        # 递归遍历
        for value in node.values():
            traverse(value)

    elif isinstance(node, list):
        for item in node:
            traverse(item)


if __name__ == "__main__":
    code = """
    function add(a, b) {
        const result = 100 + a + b;
        return result;
    }
    console.log(add(10, 20));
    """

    # 解析 JS
    ast = esprima.parseScript(code, {
        "range": True
    })

    # AST 转字典
    ast_dict = ast.toDict()

    # 递归遍历 AST，修改函数名和变量名
    traverse(ast_dict)

    print("变量映射：")
    print(json.dumps(name_map, indent=4))

    # 重新生成 JS
    print("\n混淆后的代码：")
    print(escodegen.generate(ast_dict))
