from googleads import adwords
import pandas as pd
import numpy as np

# Path for output file.
PATH = '/CampaignStats.csv'


def main(client, path):
  # Initialize appropriate service.
  report_downloader = client.GetReportDownloader(version='v201607')

  # Create report query.
  report_query = ('SELECT CampaignName, Impressions, Clicks, Cost, '
                  'Conversions '
                  'FROM CRITERIA_PERFORMANCE_REPORT '
                  'WHERE Clicks > 0 '
                  'DURING 20160725,20160918')

  with open(path, 'w') as output_file:
    report_downloader.DownloadReportWithAwql(
        report_query, 'CSV', output_file, skip_report_header=False,
        skip_column_header=False, skip_report_summary=False)

  print('Report was downloaded to \'%s\'.' % path)

def compileCampStats(path):
  df = pd.read_csv(path,skiprows=[0])
  df.head()
  table = pd.pivot_table(df,index="Campaign",values=["Impressions","Clicks","Cost","Conversions"],aggfunc=np.sum)
  table.to_csv("CompiledCampStats.csv",sep='\t', encoding='utf-8')

if __name__ == '__main__':
  # Initialize client object.
  adwords_client = adwords.AdWordsClient.LoadFromStorage()

  main(adwords_client, PATH)
  compileCampStats(PATH)


