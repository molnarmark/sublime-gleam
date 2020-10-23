import sublime
import sublime_plugin
import subprocess
import os

SETTINGS_FILE = 'gleam.sublime-settings'

def format(path):
  result = subprocess.call(["gleam", "format", path])
  if result == 0:
    print('Successfully formatted Gleam code.')
  else:
    print('Something went wrong. Gleam format exited with error code', result)

class GleamFmtCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    return format(self.view.file_name())

class GleamRunOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):
      settings = sublime.load_settings(SETTINGS_FILE)
      filepath = view.file_name()

      if not filepath:
        return 0

      print(settings.get('format_on_save'))
      file_extension = os.path.splitext(filepath)[1][1:]
      if file_extension == 'gleam' and settings.get('format_on_save'):
        return format(view.file_name())