import reflex as rx

# Comun

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

_meta=[
        {"name": "og:type", "content": "website"},
        #{"name": ""},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@juanppdev"}
    ]

# Index
index_title="Juanppdev | Aprendiendo cada dia juntos"
index_description="Hola, mi nombre es Juanppdev"

index_meta= [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

# Projects
projects_title="Juanppdev | Proyectos"
projects_description="Hola, mi nombre es Juanppdev y estos son mis proyectos"

projects_meta= [
    {"name": "og:title", "content": projects_title},
    {"name": "og:description", "content": projects_description},
]
projects_meta.extend(_meta)