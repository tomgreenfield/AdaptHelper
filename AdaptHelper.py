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

	def is_visible(self, **args):
		if args.get("redo"): return hasattr(self, "cmd_name")

		dirs = args["dirs"]
		cmd_name = args.get("cmd_name")

		if not len(dirs) > 0: return False
		if not cmd_name: return True

		if "grunt" in cmd_name: required_file = "Gruntfile.js"
		elif "gulp" in cmd_name: required_file = "gulpfile.js"
		else: return True

		return os.path.isfile(os.path.join(dirs[0], required_file)) and \
			os.path.isdir(os.path.join(dirs[0], "node_modules"))

	def description(self, **args):
		if args.get("redo") and hasattr(self, "cmd_name"):
			return "Redo \"" + self.cmd_name + "\""

		return ""