import time

def runing_string(window, text):
	text = text + "    "
	arr = [" " for i in range(len(text))]
	e = 0
	while True:
		arr = arr[1:]
		arr.append(text[e])
		e += 1
		if e == len(text):
			e = 0

		window.set_title("".join(arr))
		time.sleep(0.1)

def animate_ico(window, paths):
	while True:
		for path in paths:
			window.set_icon(path)
			time.sleep(1)


if __name__ == "__main__":
	from Engine import Window, Color, Console
	import threading, random

	def task():
		w = Window(random.randint(20, 60), random.randint(15, 30))
		threading.Thread(target=runing_string, args=(w, str(random.randint(100000,10000000000)))).start()
		threading.Thread(target=animate_ico, args=(w, ["icons/1.ico","icons/2.ico","icons/3.ico","icons/4.ico"])).start()
		while True:
			time.sleep(1 * random.random())
			w.fill(Color.rgb_background(random.randint(0, 255),random.randint(0,255),random.randint(0,255))+"#")
			w.print()

	for i in range(5):
		threading.Thread(target=task).start()