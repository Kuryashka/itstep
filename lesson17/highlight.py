def highlight(text: str, str_to_select: str, decoration: str) -> str:
    return text.replace(str_to_select, decoration + str_to_select + decoration)

  if __name__ == '__main__':
  print(highlight('kfdf', 'd', '*'))
