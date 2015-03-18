import sublime
import sublime_plugin

class RunCommandHereCommand(sublime_plugin.WindowCommand):
	def run(self, **args):
		self.dir = args["dirs"][0]
		self.cmd_name = args.get("cmd_name") or ""
		self.separator = args.get("separator") or ""
		label = args.get("label")

		if label:
			self.window.show_input_panel(label, "", self.execute, None, None)
		else:
			self.execute(None)

	def execute(self, input):
		if input: self.cmd_name += self.separator + input

		if not self.cmd_name: return

		self.window.run_command("exec", {
			"cmd": self.cmd_name, "shell": True, "working_dir": self.dir
		})
		sublime.status_message("Running " + self.cmd_name)

	def is_visible(self, **args):
		return len(args["dirs"]) > 0

class KillCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.run_command("exec", { "kill": True })