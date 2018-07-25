from PyQt5.QtCore import QRunnable, pyqtSlot
from libs.WorkerSignals import WorkerSignals
import traceback, sys

class Worker(QRunnable):
	'''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and 
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

	def __init__ (self, fn, params):
		super(Worker, self).__init__()

		# store constructor arguments (re-used for processing)
		self.fn = fn
		self.params = params
		self.signals = WorkerSignals()


	@pyqtSlot()
	def run(self):
		'''
		Initialise the runner function with passed args, kwargs.
		'''

		# Retrieve args/kwargs here; and fire processing using them
		try:
			result = self.fn(self.params)
		except:
		    traceback.print_exc()
		    exctype, value = sys.exc_info()[:2]
		    self.signals.error.emit((exctype, value, traceback.format_exc()))
		else:
		    self.signals.result.emit(result)  # Return the result of the processing
		finally:
		    self.signals.finished.emit()  # Done