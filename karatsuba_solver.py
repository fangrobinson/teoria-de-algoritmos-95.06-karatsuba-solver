import math
DEFAULT_BASE = 10

class KaratsubaSolver():

	def __init__(self, base):
		self.base = base
		self.sum_amount = 0
		self.mult_amount = 0
		self.strs = []

	def get_sum_amount(self):
		return self.sum_amount


	def get_mult_amount(self):
		return self.mult_amount


	def _normalized_len(self, n):
		len_n = len(str(n))
		return len_n


	def _most_sig(self, n, max_len):
		return int(n // (self.base ** math.ceil(max_len // 2)))


	def _less_sig(self, n, max_len):
		return int(n % (self.base ** math.ceil(max_len // 2)))


	def _combine_res(self, n, m, n1m1, max_len, p, n0m0):
		self.sum_amount += 4
		return int(n1m1 * (self.base ** (max_len // 2 * 2)) + (p - n1m1 - n0m0) * (self.base ** math.ceil(max_len // 2)) + n0m0)


	def _base_case(self, n, m):
		self.mult_amount += 1
		self.strs.append(f"Caso base: k({n}, {m}) = {n * m}\n")
		return n * m


	def multiply(self, n, m):
		max_len = max(self._normalized_len(n), self._normalized_len(m))

		if n < 10 and m < 10:
			return self._base_case(n, m)

		n1 = self._most_sig(n, max_len)
		m1 = self._most_sig(m, max_len)

		n0 = self._less_sig(n, max_len)
		m0 = self._less_sig(m, max_len)

		p = self.multiply(n1 + n0, m1 + m0)
		self.sum_amount += 2

		n1m1 = self.multiply(n1, m1)
		n0m0 = self.multiply(n0, m0)

		res = self._combine_res(n, m, n1m1, max_len, p, n0m0)

		k_string = f"k({n}, {m})\n"
		K_N_str = f" - N = {max_len}\n"
		n1_str = f" - n1 = {n1}\n"
		n0_str = f" - n0 = {n0}\n"
		m1_str = f" - m1 = {m1}\n"
		m0_str = f" - m1 = {m0}\n"
		n1m1_str = f" - n1 * m1 = k({n1}, {m1})\n"
		n0m0_str = f" - n0 * m0 = k({n0}, {m0})\n"
		result_str = f" - k({n}, {m}) = {n1m1} * 10^{(max_len // 2 * 2)} + (P - {n1m1} - {n0m0}) * 10^{math.ceil(max_len // 2)} + {n0m0} = {res}\n"

		self.strs.append(k_string + K_N_str + n1_str + n0_str + m1_str + m0_str + n1m1_str + n0m0_str + result_str)
		return res
		


class KaratsubaNumberGenerator():

	def get_n_and_m(self, id):
		n = 3504110
		a = id % 10
		b = id % 1000 // 100
		c = int(str(id)[0:2]) % 7
		n += a * (10 ** 7)
		n += b * (10 ** 4)
		n += c

		m = 20980055
		d = id % 100 // 10
		e = id % 10000 // 1000
		f = int(str(id)[len(str(id))-2:]) % 9
		m += d * (10 ** 6)
		m += e * (10 ** 3)
		m += f * (10 ** 2)
		return n, m


def main():
	padron = 97009
	n, m = KaratsubaNumberGenerator().get_n_and_m(97009)
	assert(n == 93504116)
	assert(m == 20987055)
	k = KaratsubaSolver(DEFAULT_BASE)
	k_res = k.multiply(9350411693504116, 2098705520987055)
	mul_res = n * m
	print(f"k: {k_res}")
	print(f"mul: {mul_res}")
	print(f"sum_amount: {k.get_sum_amount()}")
	print(f"mult_amount: {k.get_mult_amount()}")
	# assert(k_res == mul_res)

	for _str in k.strs[::-1]:
		print(_str)

if __name__ == '__main__':
	main()



