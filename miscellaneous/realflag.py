import zlib, base64

TANAKA = "eJyNVG1320QT/Z5z8h+GhNYvcR35JZZdaCGhT6D0gQTiFKjjlpU0ljZe7272xYpoy2/vrJRA+MA56IOPrJ29e+feO7sP84JJ2CohsEqYELBlktsCWM64tA6E3+gKEjSm6u/uXBzPz+AZtBY/vRx91Unffv908vOrw9PXz7/E23h/nf2mtp9/Gz05fn9zbv8sB18f/P7DWa9o/5/1f/Hf6KMlhzfJ9YvZ/x4NKzk185PNF6vud3uf/Xjx0eV/PLsUvz4ev/tw1bq6au3u7MNxorYIK5Yi4K0WRAhWyoAuKstTJiDDlFuuZB9C9WvOwEq2RpBsg2CUlxk4Is5XPIXEMGubwlNqVpVc5mB9nqN1BAG2LjeYM5OFpRVumCAUTPF+31yVtAhb+oB0OLcsN4ikjUTmCih8jqCVoSODUpdvLl+9JK0W8fhJdBD1dnfg7pnG3UGPS9ceT7vdQYdW9uFstQLtjVYWQTBiwiwYb6hJ65jDDUpHoPcIYfP03ahTo4yG/Sg8zb/WaNwKkPel8QQeQ3R7etqLh/CB3qKoF8/gbfO2mBwtF9GypvDCm9D4WipHbYsKLCP1S4MuLTADmzISw6gyiHGP3h52euMY+ArmxpNLguhHNY/B8JBaG0TwCAaDnjJZOy1MezjpPCQ3ig6O7pQ4HHYJa9adLQMXOBfeglMIFp0jH0pOCm8ZBZJSialrHIGLQJECnFmwBQqSvqk0zLkKtFGZT5GEo9Iz7yzPSF3MLUhynYw0NpximLzxXISmWchCU39soWRiDZqRHE04eF64lRfAsi0n2JrCCdaomlXBowBGKU0qMtFQHNYYpmYfzgPzBAu25SHAiv65Jk1esoT6K9TmDhCON4psoLhT7FO1aXKfKhnOqR3ykjwq6Zs3pslFG8K+hqXVzKzJLWVSmuJ6gqxWQY7cMF0fEqRvtWjLpSTIJr3XWFKo00Jp6oXoZaiRVqklmh8RNAy7+uHnWhGhf33ai7/9DQ5xWfeRlJiA4wiKkl544yjYoZu7S2XBl38h/Ldd4SbglAZoJu3hoRRHDs9hHA+nT/9Bhp7EIFs//OhoRoej8WQSQxemo3h69HBV02mu7Q5H46M4no46tUPzgqTOC7jxiBIytiF6YAXXGk1Ve8YMt3WQls2OkyqEKQyzUXRBhYwqT83QQKGjJVtQbVN6pike3CFUoVIijV7SZMx6wk/CjUzXcfCxIbe3Eip/P91e46z0MtGz6fjjHmHt7nwCLpe/Qg=="
TAKAHASHI = [0x7a,0x7a,0x7a,0x12,0x18,0x12,0x1d,0x12,0x07,0x7b,0x36,0x37,0x3c,0x30,0x36,0x37,0x67,0x65,0x31,0x7d,0x67,0x65,0x36,0x20,0x32,0x31,0x7b,0x20,0x20,0x36,0x21,0x23,0x3e,0x3c,0x30,0x36,0x37,0x7d,0x31,0x3a,0x3f,0x29,0x7b,0x30,0x36,0x2b,0x36]
print(zlib.decompress(base64.b64decode(TANAKA)))
# 定義されたSATO文字列
SATO = '[QI3?)c^J:6RK/FV><ex7#kdYov$G0-A{qPs~w1@+`MO,h(La.WuCp5]i ZbjD9E%2yn8rTBm;f*H"!NS}tgz=UlX&4_|\\\'\\'

# SUZUKIリストの定義、計算式やビット演算を含む
SUZUKI = [74-0+0,
          87*1,int(48**1),
          int(83),int(32.00000),int('34'),
          76 & 0xFF,72 | 0x00,79 ^ 0x00,[65][0],
          (2),47 if True else 0,int(12/1),10 % 11,ord(chr(26)),
          30+5,int(48/2*2),9*9]

# SATOリストからSUZUKIインデックスに基づいて文字を取得し、結合して出力
result = ''.join([SATO[i] for i in SUZUKI])
print(result)

