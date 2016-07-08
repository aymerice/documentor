cmake_minimum_required(VERSION 2.8)
project(documentor)


add_custom_target(html ALL)
add_custom_target(plantuml_files)
add_custom_target(images)


set(unified_schema "${CMAKE_CURRENT_SOURCE_DIR}/unified.extschema.json")
set(docs_source_dir "${CMAKE_CURRENT_SOURCE_DIR}/docs_src")
set(docs_destiny_dir "${CMAKE_CURRENT_BINARY_DIR}/docs")
set(docs_work_dir "${CMAKE_CURRENT_BINARY_DIR}/docs_tmp")
set(img_dir "${docs_work_dir}/img")


file(GLOB json_tables
	RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}/common/"
	"${CMAKE_CURRENT_SOURCE_DIR}/common/*.json"
)

# Prepare docs dir
file(MAKE_DIRECTORY ${docs_work_dir})
file(MAKE_DIRECTORY "${docs_work_dir}/_static")
file(MAKE_DIRECTORY ${img_dir})
file(MAKE_DIRECTORY ${docs_destiny_dir})
file(COPY "${docs_source_dir}/conf.py" DESTINATION ${docs_work_dir})
file(COPY "${docs_source_dir}/Makefile" DESTINATION ${docs_work_dir})


# Generate PlantUML txt files
set(documentor "${docs_source_dir}/documentor.py")
foreach(json ${json_tables})
	string(REPLACE ".json" ".txt" txt_out ${json})
	set(txt_out "${img_dir}/${txt_out}")
	string(REPLACE "/" "__" target ${txt_out})

	add_custom_command(
		OUTPUT ${txt_out}
		COMMAND ${documentor} ARGS --output-dir ${docs_work_dir} ${unified_schema}
		DEPENDS ${documentor} ${unified_schema}
	)

	add_custom_target(generate-${target} DEPENDS ${txt_out})
	add_dependencies(plantuml_files generate-${target})
endforeach(json)


# Generate PNG diagrams
set(jar_file "${docs_source_dir}/plantuml.jar")
function(generate_img_png JSON_SRC)
	string(REGEX REPLACE ".json" ".txt" txt_file ${JSON_SRC})
	string(REGEX REPLACE ".json" ".png" png_file ${JSON_SRC})
	set(in_path ${img_dir}/${txt_file})
	set(out_path ${img_dir}/${png_file})
	string(REGEX REPLACE "/" "__" target ${out_path})

	add_custom_command(
		OUTPUT ${out_path}
		COMMAND java ARGS -Djava.awt.headless=true -jar ${jar_file} ${in_path}
		DEPENDS ${jar_file} ${in_path}
	)

	add_custom_target(generate-${target} DEPENDS ${out_path})
	add_dependencies(generate-${target} plantuml_files)
	add_dependencies(images generate-${target})
endfunction(generate_img_png)

foreach(json ${json_tables})
	generate_img_png(${json})
endforeach(json)


# Generate HTML documentation
set(index "${docs_work_dir}/_build/html/index.html")
string(REPLACE "/" "__" index_target ${index})
add_custom_command(
	OUTPUT ${index}
	COMMAND make ARGS html
	WORKING_DIRECTORY ${docs_work_dir}
	DEPENDS ${unified_schema}
)
add_custom_target(generate-${index_target} DEPENDS ${index})
add_dependencies(generate-${index_target} images plantuml_files)
add_dependencies(html generate-${index_target})

add_custom_command(TARGET html POST_BUILD
	COMMAND ${CMAKE_COMMAND} -E copy_directory "${docs_work_dir}/_build/html" ${docs_destiny_dir}
)
