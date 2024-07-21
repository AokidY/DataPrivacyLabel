import requests
import json
import os

if __name__  == "__main__":

    post_url = 'https://api.openai.com/v1/chat/completions'
    api_key = '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'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    #need to change
    path_txt = '/Users/zachary/Documents/uci/221dataPriva/project/work/health/file_txt/'
    #need to change
    app_name = 'stoic'

    filename = app_name + '_content' + '.txt'


    filepath = os.path.join(path_txt, filename)

    with open(filepath, 'r', encoding='utf-8') as fp:
        local_text = fp.read()

    input_text = f'Please generate the privacy labels based on the following contents : {local_text}. \
                    and there are some label cases like Usage Data, Diagnostics, Identifiers, Purchases, location, user content, search history, contact info, Heath&Fitness, Data retention, Data deletion that you can use\
                    In addition to the label examples I provided above, you can also provide some additional labels that related to the policy contents I provided. \
                    If there is no content corresponding to these labels in the privacy policy, please display None. '
    data = {
        'model' : 'gpt-3.5-turbo',
        'messages' : [{'role': 'user', 'content': input_text}]
    }
    response = requests.post(url = post_url, json = data, headers = headers)
    generated_text = response.json()


    #need to change
    path_json_final = '/Users/zachary/Documents/uci/221dataPriva/project/work/health/final_gpt_results/json_file/'
    path_txt_final = '/Users/zachary/Documents/uci/221dataPriva/project/work/health/final_gpt_results/txt_file/'
   
    
    
    file_json_name = app_name + '_content' + '.json'
    file_txt_name = app_name + '_content' + '.txt'


    json_path = os.path.join(path_json_final, file_json_name)
    txt_path = os.path.join(path_txt_final, file_txt_name)


    with open(json_path, 'w', encoding = 'utf-8') as fp:
        json.dump(generated_text, fp = fp, ensure_ascii = False)

    with open(json_path, 'r', encoding='utf-8') as fp:
        json_data = json.load(fp)

    main_content = json_data['choices'][0]['message']['content']

    with open(txt_path, 'w', encoding='utf-8') as fp:
        fp.write(main_content)


    print("End!")
