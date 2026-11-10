# main.py
from infrastructure.database import Database
from infrastructure.student_repository import StudentRepository
from usecases.student_usecase import StudentUseCase
from presentation.views.student_view import StudentView
from presentation.views.controllers.student_controller import StudentController
def main():
    db = Database(host="localhost", user="root", password="", 
database="db_kampus")
    repo = StudentRepository(db)
    usecase = StudentUseCase(repo)
    view = StudentView()
    controller = StudentController(usecase, view)
    controller.load_students()
    view.mainloop()
if __name__ == "__main__":
    main()