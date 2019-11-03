import lxml.etree as LET #to use on xslt
import xml.etree.ElementTree as ET
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import RelatarForm
from lxml import etree


def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')


def relatar(request):
    form = RelatarForm()
    return render(request, 'relatar.html', {'form': form})
    #return render(request, 'relatar.html')


def estatisticas(request):
    month = get_occmonth()
    return render(request, 'estatisticas.html', {'month': month})


def avisos(request):
    return render(request, 'avisos.html')

def listar(request):
    return render(request, 'fogos_recentes.html')

def get_occmonth():
    tree = ET.parse('app/xml/db.xml')
    root = tree.getroot()
    months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for c in root.findall('incidente'):
        months[int(c.find('DataOcorrencia').text[5:7])-1] += 1
    return months

#lista de fogos que estao a ocorrer --> usar xpath (so para usar sem ser com a bd) e assim mostra uma lista de fogos sem ser no mapa
def fogos_recentes_lista(request):
    template = loader.get_template('fogos_recentes.html')

    dic = {}
    tree = ET.parse('app/xml/db.xml')
    root = tree.getroot()
    for c in root.findall('incidente'):
        dic.update({c.find('Localidade').text: c.find('DataOcorrencia').text})

    context = {
        'info': dic,
    }
    return HttpResponse(template.render(context, request))


#mostrar detalhes dos incendios descritos na função fogos_recentes_lista (para um especifico selecionado)
def get_fogo(xml_file: str, value: str):
    dic = {}
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for c in root.findall('fogo'):
        if c.find("Localidade").text == value:
            dic = {
                'DataOcorrencia': c.find('DataOcorrencia').text,
                'Natureza': c.find('Natureza').text,
                'Estado': c.find('Estado').text,
                'Distrito': c.find('Distrito').text,
                'Concelho': c.find('Concelho').text,
                'Freguesia': c.find('Freguesia').text,
                'Localidade': c.find('Localidade').text,
                'Latitude': c.find('Latitude').text,
                'Longitude': c.find('Longitude').text,
                'MeiosTerrestres': c.find('MeiosTerrestres').text,
                'OperacionaisTerrestres': c.find('OperacionaisTerrestres').text,
                'MeiosAereos': c.find('MeiosAereos').text,
                'OperacionaisAereos': c.find('OperacionaisAereos').text,
            }
            break
    return dic

#mostrar detalhes dos incendios descritos na função fogos_recentes_lista (para um especifico selecionado)
def mostrar_detalhes(request):
    template = loader.get_template('detalhes.html')
    value = request.GET.get('localidade')
    context = get_fogo("xml/db.xml", value)
    return HttpResponse(template.render(context, request))

def storeData(request):
    if request.method == 'POST':
        form = RelatarForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print(form)
            data = form.cleaned_data
            for k in data:
                print('{} : {}'.format(k, data[k]))
            return HttpResponse(status=204)
            #return HttpResponseRedirect('/thanks/')
        else:
            print('not valid')
            #return HttpResponseRedirect('/thanks/')
    return HttpResponse(status=204)


#validate a xml file with xml schema
def validate(file_xml: str, file_schema: str):
    # parsing xsd
    with open(file_schema, 'r') as schema_file:
        xmlschema_doc = etree.parse(schema_file)
        xmlschema = etree.XMLSchema(xmlschema_doc)

        # parsing xml
        with open(file_xml, 'r') as xml_file:
            try:
                doc = etree.parse(xml_file)
                print('XML well formed, syntax ok.')

            # check for file IO error
            except IOError:
                print('Invalid File')

            # check for XML syntax errors
            except etree.XMLSyntaxError as err:
                print('XML Syntax Error, see error_syntax.log')
                with open('error_syntax.log', 'w') as error_log_file:
                    error_log_file.write(str(err.error_log))
                quit()

            except:
                print('Unknown error, exiting.')
                quit()

        # validate against schema
        try:
            xmlschema.assertValid(doc)
            print('XML valid, schema validation ok.')

        except etree.DocumentInvalid as err:
            print('Schema validation error, see error_schema.log')
            with open('error_schema.log', 'w') as error_log_file:
                error_log_file.write(str(err.error_log))
            quit()

        except:
            print('Unknown error, exiting.')
            quit()

        # validate schema
        try:
            xmlschema.assertValid(doc)
            print('XML valid, schema validation ok.')

        except etree.DocumentInvalid as err:
            print('Schema validation error, see error_schema.log')
            with open('error_schema.log', 'w') as error_log_file:
                error_log_file.write(str(err.error_log))
            quit()

        except:
            print('Unknown error, exiting.')
            quit()


#pagina html gerada com xslt depois dos dados serem inserios através do formulario (já passaram por uma verificação)
# esta pagina apenas vai indicar se o incendio relatado foi aceite ou nao
#def confirmData():





