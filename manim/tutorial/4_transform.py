from manimlib.imports import *
class WhatIsTransform(Scene):
	def construct(self):
		M1 = TextMobject("A")
		M2 = TextMobject("B")
		M3 = TextMobject("C")
		M4 = TextMobject("D")

		self.play(Write(M1))
		self.wait()

		self.play(Transform(M1, M2))
		self.wait()

		self.play(Transform(M1, M3))
		self.wait()

		self.play(Transform(M1, M4))
		self.wait()

		self.play(FadeOut(M1))  # 上述三个操作依次将 M1 赋值为 M2 ， M3 ， M4
		self.wait()
		M1 = TextMobject("A")
		self.play(Write(M1))
		self.wait()
		self.play(ReplacementTransform(M1, M2))  # 从 M1 变动到 M2, 字符长度不会影响变化过程
		self.wait()
		self.play(ReplacementTransform(M2, M3))  # 从 M2 变动到 M3, 字符长度不会影响变化过程
		self.wait()
		self.play(ReplacementTransform(M3, M4))  # 从 M3 变动到 M4, 字符长度不会影响变化过程
		self.wait()
		self.play(FadeOut(M4))
		self.wait()
		# 上述的两个部分达到的动画效果相同，但是第一个改变了 M1 内部的值， 第二个则没有改变

class TransformationText1V1(Scene):
	def construct(self):
		texto1 = TextMobject("First text")
		texto2 = TextMobject("Second text")
		self.play(Write(texto1))
		self.wait()
		self.play(Transform(texto1, texto2))  # texto1 会在原始位置上消失，然后替换成为texto2
		self.wait()

class TransformationText1V2(Scene):
	def construct(self):
		texto1 = TextMobject("First text")
		texto1.to_edge(UP)
		texto2 = TextMobject("Second text")
		self.play(Write(texto1))
		self.wait()
		self.play(Transform(texto1,texto2))
		self.wait()

class TransformationText2(Scene):
	def construct(self):
		text1 = TextMobject("Function")
		text2 = TextMobject("Derivative")
		text3 = TextMobject("Integral")
		text4 = TextMobject("Transformation")
		self.play(Write(text1))
		self.wait()
		#Trans text1 -> text2
		self.play(ReplacementTransform(text1, text2))
		self.wait()
		#Trans text2 -> text3
		self.play(ReplacementTransform(text2, text3))
		self.wait()
		#Trans text3 -> text4
		self.play(ReplacementTransform(text3, text4))
		self.wait()

class CopyTextV1(Scene):
	def construct(self):
		formula = TexMobject(
			"\\frac{d}{dx}", #0
			"(", #1
			"u", #2
			"+", #3
			"v", #4
			")", #5
			"=", #6
			"\\frac{d}{dx}", #7
			"u", #8
			"+", #9
			"\\frac{d}{dx}", #10
			"v" #11
			)
		formula.scale(2)
		self.play(Write(formula[0:7]))  # 这里的write 顺序是从左到右,第七个 是不会被打印出的
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(), formula[8]),
			ReplacementTransform(formula[4].copy(), formula[11]),
			ReplacementTransform(formula[3].copy(), formula[9])
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(), formula[7]),
			ReplacementTransform(formula[0].copy(), formula[10])
			)
		self.wait()

class CopyTextV2(Scene):
	def construct(self):
		formula = TexMobject(
			"\\frac{d}{dx}",
			"(",
			"u",
			"+",
			"v",
			")",
			"=",
			"\\frac{d}{dx}",
			"u",
			"+",
			"\\frac{d}{dx}",
			"v"
			)
		formula.scale(2)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
		self.wait()

class CopyTextV3(Scene):
	def construct(self):
		formula = TexMobject("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		formula[8].set_color(RED)
		formula[11].set_color(BLUE)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
		self.wait()

class CopyTextV4(Scene):
	def construct(self):
		formula = TexMobject("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		for letter,color in [("u",RED),("v",BLUE)]:
			formula.set_color_by_tex(letter,color)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
		self.wait()

class CopyTwoFormulas1(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg",		#0
				"\\forall",		#1
				"x",			#2
				":",			#3
				"P(x)"			#4
			)
		formula2 = TexMobject(
				"\\exists",		#0
				"x",			#1
				":",			#2
				"\\neg",		#3
				"P(x)"			#4
			)
		for size, pos, formula in [
			(2, 2*UP, formula1),
			(2, 2*DOWN, formula2)
		]:
			formula.scale(size)
			formula.move_to(pos)
		self.play(Write(formula1))
		self.wait()
		changes = [
			[(0,1,2,3,4),
			# | | | | |
			# v v v v v
			 (3,0,1,2,4)],
		]
		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()

class CopyTwoFormulas2(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg","\\forall","x",":","P(x)"
			)
		formula2 = TexMobject(
				"\\exists","x",":","\\neg","P(x)"
			)
		for tam,pos,formula in [(2,2*UP,formula1),(2,2*DOWN,formula2)]:
			formula.scale(tam)
			formula.move_to(pos)
		self.play(Write(formula1))
		self.wait()
		changes = [
			# First time
			[(2,3,4),
			# | | |
			# v v v
			 (1,2,4)],
			# Second time
			[(0,),
			# | 
			# v
			 (3,)],
			# Third time
			[(1,),
			# | 
			# v
			 (0,)]
		]
		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()

class CopyTwoFormulas2Color(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg","\\forall","x",":","P(x)"
			)
		formula2 = TexMobject(
				"\\exists","x",":","\\neg","P(x)"
			)
		parametters = [(2,2*UP,formula1,GREEN,"\\forall"),
					  (2,2*DOWN,formula2,ORANGE,"\\exists")]
		for size,pos,formula,col,sim in parametters:
			formula.scale(size)
			formula.move_to(pos)
			formula.set_color_by_tex(sim,col)
			formula.set_color_by_tex("\\neg",PINK)
		self.play(Write(formula1))
		self.wait()
		changes = [
			[(2,3,4),(1,2,4)],
			[(0,),(3,)],
			[(1,),(0,)]
		]
		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()

class CopyTwoFormulas3(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg","\\forall","x",":","P(x)"
			)
		formula2 = TexMobject(
				"\\exists","x",":","\\neg","P(x)"
			)
		parametters = [(2,2*UP,formula1,GREEN,"\\forall"),
					  (2,2*DOWN,formula2,ORANGE,"\\exists")]
		for size,pos,formula,col,sim in parametters:
			formula.scale(size)
			formula.move_to(pos)
			formula.set_color_by_tex(sim,col)
			formula.set_color_by_tex("\\neg",PINK)
		self.play(Write(formula1))
		self.wait()
		changes = [
			[(2,3,4),(1,2,4)],
			[(0,),(3,)],
			[(1,),(0,)]
		]
		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					formula1[i],formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()

class ChangeTextColorAnimation(Scene):
	def construct(self):
		text = TextMobject("Text")
		text.scale(3)
		self.play(Write(text))
		self.wait()
		self.play(
                text.set_color, YELLOW,
                run_time=2
            )
		self.wait()

class ChangeSizeAnimation(Scene):
	def construct(self):
		text = TextMobject("Text")
		text.scale(2)
		self.play(Write(text))
		self.wait()
		self.play(
                text.scale, 3,
                run_time=2
            )
		self.wait()

class MoveText(Scene):
	def construct(self):
		text = TextMobject("Text")
		text.scale(2)
		text.shift(LEFT*2)
		self.play(Write(text))
		self.wait()
		self.play(
                text.shift, RIGHT*2,
                run_time=2,
                path_arc=0 #Change 0 by -np.pi
            )
		self.wait()

class ChangeColorAndSizeAnimation(Scene):
	"""
	首先在屏幕上显示 写出text 的动画
	然后 向右移动 两个单位
	放大为原来的两倍
	将字体颜色设置为红色
	"""
	def construct(self):
		text = TextMobject("Text")
		text.scale(2)
		text.shift(LEFT*2)
		self.play(Write(text))
		self.wait()
		self.play(
                text.shift, RIGHT*2,
                text.scale, 2,
                text.set_color, RED,
                run_time=3,
            )
		self.wait()


class ChangeColorAndSizeAnimation2(Scene):
	"""
	首先在屏幕上显示 写出text 的动画
	然后 向右移动 两个单位
	放大为原来的两倍
	将字体颜色设置为红色

	效果和上面的相同，但代码更加简洁，首先定义 Object的target 的完全体，然后调用 MoveTOTarget 进行原始 Object 到 TargetObject的动画
	"""
	def construct(self):
		text = TextMobject("Text")
		text.scale(2)
		text.shift(LEFT*2)
		self.play(Write(text))
		self.wait()
		text.generate_target()
		text.target.shift(RIGHT * 2)
		text.target.scale(2)
		text.target.set_color(RED)
		self.play(
				MoveToTarget(text),
                run_time=3,
            )
		self.wait()


class SumDC(Scene):
	def construct(self):
		list1 = TexMobject(r"1+2+3+4+\cdots +n=?")
		list2 = TexMobject(r"a_1+a_2+a_3+a_4+\cdots +a_n=?")
		desc = TexMobject(r"a_{n+1}-a_n=d")

		min1 = TexMobject(r"a_2-a_1=d")
		min1.shift(2 * UP)
		min2 = TexMobject(r"a_3-a_2=d")
		min2.next_to(min1, DOWN)
		min3 = TexMobject(r"a_4-a_3=d")
		min3.next_to(min2, DOWN)
		min4 = TexMobject(r"\cdots")
		min4.next_to(min3, DOWN)
		min5 = TexMobject(r"a_n-a_{n-1}=d")
		min5.next_to(min4, DOWN)
		minn = VGroup(min1, min2, min3, min4, min5)

		summ = TexMobject(r"a_n-a_1=\left( n-1 \right) d")
		summ2 = TexMobject(r"a_n=a_1+\left( n-1 \right) d")

		self.play(Write(list1))
		self.wait(2)
		self.play(Transform(list1, list2))
		self.wait(2)
		self.play(ApplyMethod(list1.shift, 3 * UP))
		self.play(Write(minn))
		self.wait(2)
		self.play(Transform(minn, summ))
		self.wait(2)
		self.play(Transform(minn, summ2))