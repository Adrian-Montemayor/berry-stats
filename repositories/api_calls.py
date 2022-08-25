import requests 
from matplotlib import pyplot as plt
from settings import settings

class ApiCalls:
    @staticmethod
    def get_berries(endpoint):
        berry_list = {
            "berries": [],
            "min_growth_time": None,
            "median_growth_time": None,
            "max_growth_time": None,
            "variance_growth_time": None,
            "mean_growth_time": None,
            "frequency_growth_time": None,
        }
        times = []
        results = requests.get(endpoint)
        results.raise_for_status()
        results = results.json()
        for url in results["results"]:
            berry_info = requests.get(url["url"])
            berry_info.raise_for_status()
            berry_info = berry_info.json()
            berry_obj = {
                "url": settings.sprites_url + berry_info["item"]["name"],
                "name": berry_info["name"],
                "growth_time": berry_info["growth_time"]
            }
            times.append(berry_info["growth_time"])
            berry_list["berries"].append(berry_obj)
        
        berry_list["min_growth_time"] = min(times)
        berry_list["max_growth_time"] = max(times)
        berry_list["mean_growth_time"] = round(sum(times) / len(times), 2)
        deviation = [n - berry_list["mean_growth_time"] for n in times]
        squared = [n**2 for n in deviation]
        berry_list["variance_growth_time"] = round(sum(squared) / (len(squared) - 1),2)
        berry_list["frequency_growth_time"] = max(set(times), key = times.count)
        times = sorted(times)
        data_len = len(times)
        middle = (data_len - 1) // 2
        if middle % 2:
            berry_list["median_growth_time"] = times[middle]
        else:
            berry_list["median_growth_time"] = (times[middle] + times[middle + 1]) / 2.0

        histogram = {item: value for (item,value) in berry_list.items() if type(berry_list[item]) != list}
        keys = [n.split("_")[0] for n in histogram.keys()]
        plt.bar(keys, histogram.values(), color="g")
        plt.savefig('static/histo.png')
        return berry_list



    @staticmethod
    def get_berry(berry):
        berry_url = f'{settings.base_url}/{berry}'
        api_call = requests.get(berry_url)
        api_call.raise_for_status()
        data = api_call.json()
        return data
