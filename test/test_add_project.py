
from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    project = Project(name="test project")
    if project in app.project.get_project_list():
        app.project.delete(project)

    old_projects = app.project.get_project_list()
    app.project.create(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert old_projects == new_projects