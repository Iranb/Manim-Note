from manimlib.imports import *
# run command: python manim.py tutorial/2_formulas_tex.py -ps

class Formula(Scene):
    def construct(self):
        formula_tex_1 = TexMobject(r"\frac{d}{dx}f(x)=\lim _{h\rightarrow 0}{\frac {f(x+h) - f(x)}{ h } }")
        formula_tex_2 = TexMobject("\\frac{d}{dx}f(x)=\lim _{h\\rightarrow 0}{\\frac {f(x+h) - f(x)}{ h } }")
        # 注意这里是 TexMobject 不是 TextMobject   少了个 t ,这里只显示出了一个是因为两个公式完全一致
        formula_text = TextMobject("Fraction: $\\frac{d}{dx}f(x)$")
        # 注意这里使用的是 TextMobject， 在text 文本中可以插入latex 公式，只需要使用 $$ 括住即可
        formula_tex3 = TexMobject(r"""
        \begin{bmatrix} a & a \\ a & a \\ a & a \end{bmatrix}
        """)
        formula_tex_1.scale(0.5)
        formula_tex_2.scale(0.5)
        formula_tex3.scale(0.5)
        formula_text.scale(0.5)


        formula_tex_1.next_to(formula_tex_1, UP, 1)
        formula_tex_2.next_to(formula_tex_1, DOWN, 1)
        formula_text.next_to(formula_tex_2, DOWN, 1)
        formula_tex_1.scale(1.5) # scale 可以使图像放大1.5倍
        formula_tex3.next_to(formula_text, DOWN, 1)

        self.add(formula_tex_1, formula_tex_2, formula_text, formula_tex3)

