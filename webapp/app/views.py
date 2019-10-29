import lxml.etree as LET #to use on xslt
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RelatarForm
from lxml import etree


def index(request):
    return render(request, 'index.html')


def relatar(request):
    form = RelatarForm()
    return render(request, 'relatar.html', {'form': form})
    #return render(request, 'relatar.html')


def estatisticas(request):
    return render(request, 'estatisticas.html')


def avisos(request):
    return render(request, 'avisos.html')


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





