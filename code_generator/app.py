import streamlit as st
import os

from dotenv import load_dotenv

load_dotenv()

from utils import safe_write

from chains import (
    product_manager_chain,
    tech_lead_chain,
    test_lead_chain,
    file_structure_chain,
    file_path_chain,
    code_chain,
    missing_chain,
    new_classes_chain
)

st.title("Code Generator")

language = st.radio("Select Language:",
                    ["Python", "Java", "C#", "TypeScript", "Rust", "Kotlin"])

request = st.text_area('Please Detail Your Desired Use Case for Code Generation! ', height=500)
app_name = st.text_input('Enter Project Name:')
submit = st.button("submit", type="primary")

if language and submit and request and app_name:

    dir_path = app_name + '/'

    requirements = product_manager_chain.run(request)
    req_doc_path = dir_path + '/requirements' + '/requirements.txt'
    safe_write(req_doc_path, requirements)
    st.markdown(""" :blue[Business Requirements : ] """, unsafe_allow_html=True)
    st.write(requirements)

    tech_design = tech_lead_chain.run({'language': language, 'input': request})
    tech_design_path = dir_path + '/tech_design' + '/tech_design.txt'
    safe_write(tech_design_path, tech_design)
    st.markdown(""" :blue[Technical Design :] """, unsafe_allow_html=True)
    st.write(tech_design)

    test_plan = test_lead_chain.run(requirements)
    test_plan_path = dir_path + '/test_plan' + '/test_plan.txt'
    safe_write(test_plan_path, test_plan)
    st.markdown(""" :blue[Test Plan :] """, unsafe_allow_html=True)
    st.write(test_plan)

    file_structure = file_structure_chain.run({'language': language, 'input': tech_design})
    file_structure_path = dir_path + '/file_structure' + '/file_structure.txt'
    safe_write(file_structure_path, file_structure)
    st.markdown(""" :blue[File Names :] """, unsafe_allow_html=True)
    st.write(file_structure)

    files = file_path_chain.run({'language': language, 'input': file_structure})
    files_path = dir_path + '/files' + '/files.txt'
    safe_write(files_path, files)
    st.markdown(""" :blue[File Paths :] """, unsafe_allow_html=True)
    st.write(files)

    files_list = files.split('\n')

    missing = True
    missing_dict = {
        file: True for file in files_list
    }

    code_dict = {}

    while missing:

        missing = False
        new_classes_list = []

        for file in files_list:

            code_path = os.path.join(dir_path, 'code', file)
            norm_code_path = os.path.normpath(code_path)

            if not missing_dict[file]:
                safe_write(norm_code_path, code_dict[file])
                st.markdown(""" :red[Code & Unit Tests: 2nd Iteration] """, unsafe_allow_html=True)
                st.write(code_dict[file])
                continue

            code = code_chain.predict(
                language=language,
                class_structure=tech_design,
                structure=file_structure,
                file=file,
            )

            code_dict[file] = code
            response = missing_chain.run({'language': language, 'code': code})
            if '<TRUE>' in response:
                missing = missing or missing_dict[file]
            else:
                safe_write(norm_code_path, code)
                st.markdown(""" :blue[Complete Code & Unit Tests: 1st Iteration] """, unsafe_allow_html=True)
                st.write(code)
                continue

            if missing_dict[file]:
                new_classes = new_classes_chain.predict(
                    language=language,
                    class_structure=tech_design,
                    code=code
                )
                new_classes_list.append(new_classes)

        tech_design += '\n\n' + '\n\n'.join(new_classes_list)
