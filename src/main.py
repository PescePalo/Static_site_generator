from textnode import TextNode, text_type_bold
def main():
    test = TextNode("this is a text node", text_type_bold, "https://www.boot.dev")
    print(test.__repr__())

if __name__ == "__main__":
    main()