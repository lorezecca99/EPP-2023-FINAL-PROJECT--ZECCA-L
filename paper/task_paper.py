"""Task to compile 
a LaTeX document and copy it to a specified 
directory by using the pytask and pytask_latex modules."""

import shutil

import pytask
from pytask_latex import compilation_steps as cs
from ss_us.config import BLD, PAPER_DIR

@pytask.mark.latex(
    script=BLD / "latex" / "ss_us.tex",
    document=BLD / "latex" / "ss_us.pdf",
    compilation_steps=cs.latexmk(
        options=("--pdf", "--interaction=nonstopmode", "--synctex=1", "--cd"),
    ),
)
def task_compile_ss_us():
    pass

documents=["ss_us"]

for document in documents:
    #@pytask.latex.task
    #@pytask.mark.latex(
     #   document=PAPER_DIR/ f"{document}.pdf",
      #  compilation_steps=cs.latexmk(
       #     options=("--pdf", "--interaction=nonstopmode", "--synctex=1", "--cd"),
        #),
    #)
    #def task_compile_document():
     #   pass
    #print("PDF compiled")

    @pytask.mark.depends_on(
            {
        "document":PAPER_DIR/f"{document}.pdf"
            }
    )
    @pytask.mark.produces({
        BLD/"latex"
    },
    )
    def task_copy_to_root(depends_on,produces):
        """Copy a document to the root directory for easier retrieval."""
        pdf_file = depends_on["document"]
        shutil.copyfile(pdf_file,"Social_security_LZ.pdf")
        return produces
    print("PDF copied in BLD/latex")
