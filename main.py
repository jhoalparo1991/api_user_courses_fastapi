from fastapi import FastAPI
from api import users, sections, courses

app = FastAPI( 
              title="API COURSES",
              summary='Api desarrollada en el curso de desarrollo de apis con fastapi' )

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)
