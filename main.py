import xmltodict, json, os, argparse

def convert(xml_content):
    o = xmltodict.parse(xml_content)
    return json.dumps(o, indent=2)


def convert_from_xml_file(xml_filepath):
    with open(xml_filepath, "r") as xml_file:
        return convert(xml_file.read())


def convert_and_write(xml_filepath, json_filepath):
    json_content = convert_from_xml_file(xml_filepath)
    with open(json_filepath, "w") as json_file:
        json_file.write(json_content)


def main():
    parser = argparse.ArgumentParser(description="xml to json converter")
    parser.add_argument("-i", "--input-file", help="Input file to be used", required=True)
    parser.add_argument("-o", "--output-file", help="Output file to be used", required=True)
    args = vars(parser.parse_args())
    input_file, output_file = args["input_file"], args["output_file"]
    convert_and_write(input_file, output_file)


if __name__ == "__main__":
    main()
