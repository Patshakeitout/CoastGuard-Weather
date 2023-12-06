from celery import shared_task
from weatherdata.data_retrieval_metie import fetch_xml_from_url, xml_to_custom_dictionary, coast_to_dictionary
from weatherdata.urlretrieval import (get_source_urls, update_forecast_met, update_coastal_areas,
                                      update_metocean_buoy_data, update_metie_buoy_data)
from weatherdata.data_retrieval_irishlights import get_data_from_irishlights
from weatherdata.data_retrieval_buoy_metie import get_data_from_metie_buoy


@shared_task
def update_metie_forecast():
    list_of_urls = get_source_urls('xml')
    xml_records = fetch_xml_from_url(list_of_urls[0])

    forecast_data = xml_to_custom_dictionary(xml_records)

    coastal_areas = coast_to_dictionary(xml_records)

    forecast_obj, forecast_created = update_forecast_met(forecast_data)


    if forecast_created:
        for coastal_area in coastal_areas:
            update_coastal_areas(coastal_area, forecast_obj)





@shared_task
def update_irishlights_data():
    list_of_urls = get_source_urls('html')
    buoy_data = get_data_from_irishlights(list_of_urls[0])
    for buoy in buoy_data:
        update_metocean_buoy_data(buoy)

@shared_task
def update_metie_buoy_data_model():
    print("Updating met.ie buoy data")
    list_of_urls = get_source_urls('json')
    print("List of urls: ", list_of_urls)
    buoy_data = get_data_from_metie_buoy(list_of_urls[0])

    for buoy in buoy_data:
        print("Updating buoy data for buoy: ", buoy['station_id'])
        update_metie_buoy_data(buoy)

