import sublime
import sublime_plugin
import os.path

class RunCommandHereCommand(sublime_plugin.WindowCommand):
	def run(self, **args):
		if args.get("redo"): return self.execute(None)

		self.dir = args["dirs"][0]
		self.cmd_name = args.get("cmd_name", "")
		self.separator = args.get("separator", "")
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
		self.last_cmd = self.cmd_name

	def is_visible(self, **args):
		if args.get("redo"): return hasattr(self, "last_cmd")

		dirs = args["dirs"]
		required = args.get("required")

		if not len(dirs) > 0: return False
		if not required: return True

		dir = dirs[0]

		for path in required:
			if not os.path.exists(os.path.join(dir, path)): return False

		return True

	def description(self, **args):
		if args.get("redo") and hasattr(self, "last_cmd"):
			return "Redo \"" + self.last_cmd + "\""

		return ""