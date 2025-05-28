from textnode import TextNode, TextType

def main():
    node = TextNode("Click here", TextType.LINKS, "https://www.example.com")
    print(node)

main()