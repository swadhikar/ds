from xml.etree import ElementTree
import json

xml_file = './students.xml'

tree = ElementTree.parse(xml_file)
root = tree.getroot()


def _get_children_as_dict(element):
    dictionary = {
        'attributes': {k: v for k, v in element.attrib.items()}
    }

    # Extract all attributes
    children_elements = element.findall('*')
    for children_element in children_elements:
        dictionary[children_element.tag] = children_element.text
    return dictionary


def get_title():
    return root.find('title/p').text


def get_students(as_dict=True):
    all_students = []
    student_elements = root.findall('student')
    if as_dict is True:
        for student_elem in student_elements:
            student_dict = _get_children_as_dict(student_elem)
            # print(json.dumps(student_dict, indent=2))
            all_students.append(student_dict)

    return all_students


def get_teachers(as_dict=True):
    all_teachers = []
    teacher_elements = root.findall('teacher')
    if as_dict is True:
        for teacher_element in teacher_elements:
            teacher_dict = _get_children_as_dict(teacher_element)
            # print(json.dumps(teacher_dict, indent=2))
            all_teachers.append(teacher_dict)

    return all_teachers


if __name__ == '__main__':
    print(get_title())
    print(json.dumps(get_students(), indent=2))
    print(json.dumps(get_teachers(), indent=4))
