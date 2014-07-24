import sublime
import sublime_plugin


class RunCommandHereCommand(sublime_plugin.WindowCommand):
	def run(self, **args):
		self.dir = args["dirs"][0]
		self.cmd_name = ""
		self.separator = ""
		label = None

		if args.get("cmd_name"): self.cmd_name = args["cmd_name"]
		if args.get("label"): label = args["label"]
		if args.get("separator"): self.separator = args["separator"]

		if self.cmd_name and label:
			self.window.show_input_panel(label, "", self.check_input, None, None)
		elif label:
			self.window.show_input_panel(label, "", self.execute, None, None)
		else:
			self.execute(self.cmd_name)

	def check_input(self, input):
		if input: self.cmd_name += self.separator + input
		self.execute(self.cmd_name)

	def execute(self, cmd_name):
		if cmd_name:
			self.window.run_command("exec", {
				"cmd": cmd_name, "shell": True, "working_dir": self.dir
			})
			sublime.status_message("Running " + cmd_name)

	def is_visible(self, **args):
		return len(args["dirs"]) > 0


class KillCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.run_command("exec", {"kill": True})
