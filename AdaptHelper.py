import sublime
import sublime_plugin

class RunCommandHereCommand(sublime_plugin.WindowCommand):
	def run(self, **args):
		self.dir = args["dirs"][0]
		if args.get("require_input"):
			if args.get("cmd_name"):
				self.cmd_name = args["cmd_name"]
				self.window.show_input_panel("$ " + self.cmd_name, "", self.make_cmd, None, None)
			else:
				self.window.show_input_panel("$", "", self.on_done, None, None)
		elif args.get("cmd_name"):
			self.on_done(args["cmd_name"])

	def make_cmd(self, user_args):
		if self.cmd_name == "grunt": self.cmd_name += " --no-color"
		if user_args: self.cmd_name += " " + user_args
		self.on_done(self.cmd_name)

	def on_done(self, cmd_name):
		if cmd_name:
			self.window.run_command("exec", {"cmd": cmd_name, "shell": True, "working_dir": self.dir})
			sublime.status_message("Running " + cmd_name)

	def is_visible(self, **args):
		return len(args["dirs"]) > 0

class KillCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("exec", {"kill": True})