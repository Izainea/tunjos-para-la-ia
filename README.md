# Tunjos para la IA

Programa de microcredenciales sobre razonamiento, validación e inteligencia artificial en ciencias sociales y humanidades. El nombre viene del *tunjo*, la pequeña figura de oro o tumbaga que los muiscas ofrecían en lagunas y santuarios para pedir algo y hablar con sus deidades: un acto hecho con oficio, un mensaje que queda como registro y alguien que lo entrega y responde ante su comunidad. Hoy muchos le ofrecen el tunjo a la inteligencia artificial; este programa propone lo contrario: el tunjo es lo que el investigador hace, registra y defiende. Lo diseña y dicta Carlos Isaac Zainea Maya a partir de su investigación doctoral *Agencia sin imputación* y de su trabajo con corpus textuales y visuales asistido por modelos de lenguaje. Sitio: [izainea.github.io/tunjos-para-la-ia](https://izainea.github.io/tunjos-para-la-ia/).

Tesis pedagógica: quien investiga con modelos de lenguaje necesita tres cosas que se enseñan por separado o no se enseñan. Saber qué tipo de inferencia hace la máquina y cuál hace el investigador. Saber construir un flujo técnico que deje rastro auditable. Saber validar y responder por el resultado ante una comunidad. El programa integra las tres sobre corpus reales del estudiante.

Principio de diseño: cada curso se enseña con el método que enseña. El estudiante configura con la máquina, valida, registra la frontera entre ambos y entrega el registro. La evidencia de aprendizaje no es el producto sino el registro de validación.

## Cursos

Todos de dos créditos, ocho semanas y modalidad híbrida.

| Nº | Curso | Capa |
|---|---|---|
| 1 | [Las tres inferencias: razonamiento humano y razonamiento artificial](cursos/curso-1-tres-inferencias/) | Fundamentos |
| 2 | [Corpus textual: del documento al dato trazable](cursos/curso-2-corpus-textual/) | Oficio |
| 3 | [Corpus visual: del archivo a la imagen descrita](cursos/curso-3-corpus-visual/) | Oficio |
| 4 | [Codificación asistida: la máquina configura](cursos/curso-4-codificacion-asistida/) | Oficio |
| 5 | [Métodos computacionales para el sentido](cursos/curso-5-metodos-computacionales/) | Juicio |
| 6 | [Validación e interpretación: el investigador refigura](cursos/curso-6-validacion-interpretacion/) | Juicio |
| 7 | [Ética, exterioridad y gobernanza](cursos/curso-7-etica-gobernanza/) | Juicio |

## Rutas apilables

| Ruta | Cursos | Para quién |
|---|---|---|
| Fundamentos | 1, 6 | Quien ya investiga y quiere criterio, no herramientas |
| Texto | 1, 2, 4, 6 | Sociología, historia, comunicación, derecho |
| Imagen | 1, 3, 4, 6 | Estudios visuales, museos, archivos |
| Computacional | 2, 3, 5 | Quien ya tiene método y quiere escala |
| Programa completo | 1 a 7 y proyecto integrador | Posgrado y grupos de investigación |

## Estructura del repositorio

```
cursos/curso-N-slug/      README, programa/ (syllabus, semana-01..08, evaluacion, bibliografia), plantillas/, practicas/, apps/
docs/                     sitio generado (GitHub Pages). No se edita a mano.
herramientas/             guía de autoría, plantilla de mini apps y scripts
docente.md                perfil y experiencia de quien dicta el programa
build.py                  genera docs/ a partir del markdown de todos los cursos
```

Cada curso tiene además una carpeta local `propuestas/`, fuera del repositorio, con los textos para formatos de convocatoria.

## Cómo se trabaja

```
python build.py                                                 regenera el sitio
python herramientas/verificar_curso.py --todos --capturas       verifica estructura, estilo, enlaces y mini apps
python herramientas/nuevo_curso.py 8 "Título" slug              andamio de un curso nuevo
```

La norma de escritura está en [herramientas/GUIA-AUTORIA.md](herramientas/GUIA-AUTORIA.md). Las mini apps parten de [herramientas/app-base.html](herramientas/app-base.html).

## Licencia

Material docente bajo [CC BY-SA 4.0](LICENSE). Código de las prácticas y de las herramientas bajo MIT.
