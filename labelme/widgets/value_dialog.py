from qtpy import QtWidgets
from qtpy import QtCore
from qtpy import QtGui

from labelme.logger import logger
import labelme.utils


# - Editing value for key
class ValueDialog(QtWidgets.QDialog):
    def __init__(
            self,
            text="Enter value for key",
            parent=None,
    ):
        super(ValueDialog, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout()

        self.edit = QtWidgets.QLineEdit()
        self.edit.setMinimumWidth(500)
        font = self.edit.font()
        font.setPointSize(16)
        self.edit.setFont(font)
        self.edit.setPlaceholderText(text)
        self.edit.setStyleSheet("QLineEdit { padding: 6 }")
        self.edit.editingFinished.connect(self.postProcess)

        layout_edit = QtWidgets.QHBoxLayout()
        layout_edit.addWidget(self.edit)
        layout.addLayout(layout_edit)

        # buttons
        self.buttonBox = bb = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal,
            self,
        )
        bb.button(bb.Ok).setIcon(labelme.utils.newIcon("done"))
        bb.button(bb.Cancel).setIcon(labelme.utils.newIcon("undo"))
        bb.accepted.connect(self.validate)
        bb.rejected.connect(self.reject)
        layout.addWidget(bb)

        self.setLayout(layout)

    def validate(self):
        self.accept()

    def postProcess(self):
        text = self.edit.text()
        if hasattr(text, "strip"):
            text = text.strip()
        else:
            text = text.trimmed()
        self.edit.setText(text)

    def popUp(self, text=None, move=True, flags=None, group_id=None):
        if text is None:
            text = self.edit.text()
        self.edit.setText(text)
        self.edit.setSelection(0, len(text))
        self.edit.setFocus(QtCore.Qt.PopupFocusReason)
        if move:
            self.move(QtGui.QCursor.pos())
        if self.exec_():
            return self.edit.text()
        else:
            return None
