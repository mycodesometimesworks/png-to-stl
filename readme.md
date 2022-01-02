1. have ansible installed locally
2. run ansible-playbook setup_application.yml
  1. this sets up directories, installs system packages, and sets up python environment
3. source ./start.sh
  1. this will assume the created virtualenv
4. to convert text to svg, modify python code and run`python text_to_svg.py`
5. to convert pngs or svgs to stl, modify playbook and run `ansible-playbook convert_png.yml`
6. slice output stl as desired
