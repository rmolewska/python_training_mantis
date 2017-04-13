from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.load_new_project_page()
        # enter values
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        # click submit button
        wd.find_element_by_css_selector("input.button").click()
        self.project_cache = None

    def delete(self, project):
        wd = self.app.wd
        self.load_projects_page()
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_xpath("//div[4]/form/input[3]").click()
        wd.find_element_by_xpath("//div[2]/form/input[4]").click()
        self.project_cache = None

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.load_projects_page()
            self.project_cache = []
            table = wd.find_elements_by_css_selector("table.width100")[1]
            rows = table.find_elements_by_tag_name("tr")[2:]
            for row in rows:
                cols = row.find_elements_by_tag_name("td")
                name = cols[0].text
                description = cols[4].text
                self.project_cache.append(Project(name=name, description=description))
        return list(self.project_cache)

    def load_new_project_page(self):
        wd = self.app.wd
        self.load_projects_page()
        wd.find_element_by_css_selector("td.form-title > form > input.button-small").click()

    def load_projects_page(self):
        wd = self.app.wd
        self.load_manage_page()
        wd.find_element_by_link_text("Manage Projects").click()

    def load_manage_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()