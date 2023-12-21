from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.input_text.text:
      cleaned_text = anvil.server.call('cleaned_text', self.input_text.text)
      self.output_text.visible = True
      self.output_text.text = "Preprocessed text: " + cleaned_text
    else:
      anvil.Notification("Please enter something!", timeout=2).show()
    pass

  def tree_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = anvil.server.call('predict_sentiment_tree', self.input_text.text)
    if self.predict_text.text:
        self.predict_text.text += f"\n{result}"
    else:
        self.predict_text.text = result
    pass

  def log_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = anvil.server.call('predict_sentiment_logistic', self.input_text.text)
    if self.predict_text.text:
        self.predict_text.text += f"\n{result}"
    else:
        self.predict_text.text = result
    pass

  def ann_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = anvil.server.call('predict_sentiment_ann', self.input_text.text)
    if self.predict_text.text:
        self.predict_text.text += f"\n{result}"
    else:
        self.predict_text.text = result
    pass

  def input_text_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.input_panel.visible = True
    pass

  def choose_model_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.input_panel.visible and self.output_text.visible:
      self.choose_label.visible = True
      self.tree_button.visible = True
      self.log_button.visible = True
      self.ann_button.visible = True
      self.linear_panel_3.visible = True
    else:
      anvil.Notification("Please input text first!", timeout=2).show()
    pass

  def report_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.input_panel.visible and self.linear_panel_3.visible:
      res = anvil.server.call('final_report', self.input_text.text)
      self.report_text.visible = True
      self.report_text.text = res
    else:
      anvil.Notification("Please input text first!", timeout=2).show()
    pass




