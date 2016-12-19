from googleads import adwords
import pandas as pd
import numpy as np

# Paths for report output files.
campaignsPath = '/Users/kggiorno/documents/proglearn/adwordsreporting/adrTest/RawADRCampaignStats.csv'
groupsPath = '/Users/kggiorno/documents/proglearn/adwordsreporting/adrTest/RawADRGroupStats.csv'
placementsPath = '/Users/kggiorno/documents/proglearn/adwordsReporting/adrTest/RawADRPlacementStats.csv'
keywordsPath = '/Users/kggiorno/documents/proglearn/adwordsReporting/adrTest/RawADRKeywordStats.csv'

# Ads automated DL on pause due to varying columns with extended text ads
# adsPath = '/Users/kggiorno/documents/proglearn/adwordsReporting/ADRAdsStats.csv'
# Geo automated DL on pause due to inability to directly query metros, have to query ID and then
# set up table to look up ID to get metro name, zip, or coordinates
# geoPath = '/Users/kggiorno/documents/proglearn/adwordsReporting/ADRGeoStats.csv'

# Initialize appropriate service.
report_downloader = adwords.AdWordsClient.LoadFromStorage().GetReportDownloader(version='v201607')

def campaignDL(client, path):
  # Create Campaigns/Device report query.
  report_query = ('SELECT CampaignName, CampaignStatus, Impressions, Clicks, Ctr, '
                  'Cost, AverageCpc, Device, Conversions, AveragePosition '
                  'FROM CAMPAIGN_PERFORMANCE_REPORT '
                  'WHERE Clicks > 0 '
                  'DURING 20160725,20161127')

  with open(path, 'w') as output_file:
    report_downloader.DownloadReportWithAwql(
        report_query, 'CSV', output_file, skip_report_header=False,
        skip_column_header=False, skip_report_summary=False)

def groupDL(client, path):
  # Create Group report query.
  report_query = ('SELECT CampaignName, AdGroupName, AdGroupStatus, Impressions, Clicks, Cost, '
                  ' Conversions, AveragePosition '
                  'FROM ADGROUP_PERFORMANCE_REPORT '
                  'WHERE Clicks > 0 '
                  'DURING 20160725,20161127')

  with open(path, 'w') as output_file:
    report_downloader.DownloadReportWithAwql(
        report_query, 'CSV', output_file, skip_report_header=False,
        skip_column_header=False, skip_report_summary=False)

def placementsDL(client,path):
  # Create Placements report query.
  report_query = ('SELECT Criteria, CampaignName, AdGroupName, Impressions, '
                  'Clicks, Cost, Conversions '
                  'FROM PLACEMENT_PERFORMANCE_REPORT '
                  'WHERE Clicks > 0 '
                  'DURING 20160725,20161127')

  with open(path, 'w') as output_file:
    report_downloader.DownloadReportWithAwql(
        report_query, 'CSV', output_file, skip_report_header=False,
        skip_column_header=False, skip_report_summary=False)

def keywordsDL(client,path):
  # Create Keywords report query.
  report_query = ('SELECT Criteria, KeywordMatchType, Status, CampaignName, '
                  'AdGroupName, Impressions, Clicks, Cost, Conversions '
                  'FROM KEYWORDS_PERFORMANCE_REPORT '
                  'WHERE Clicks > 0 '
                  'DURING 20160725,20161127')

  with open(path, 'w') as output_file:
    report_downloader.DownloadReportWithAwql(
        report_query, 'CSV', output_file, skip_report_header=False,
        skip_column_header=False, skip_report_summary=False)

""" Commented out for now, Ads are going to be harder to handle due to differing columns per extended textads

  def AdsDL(client,path):
  # Create Ads report query.
  report_query = ('SELECT Criteria, CampaignName, AdGroupName, Impressions, '
                  'Clicks, Cost, Conversions '
                  'FROM AD_PERFORMANCE_REPORT '
                  'WHERE Clicks > 0 '
                  'DURING 20160725,20160918')

  with open(path, 'w') as output_file:
    report_downloader.DownloadReportWithAwql(
        report_query, 'CSV', output_file, skip_report_header=False,
        skip_column_header=False, skip_report_summary=False)

"""

""" Commented out for now, Geo on pause due to needing to query ID and then use ID to look up metro name rather
    than being able to query metro name/zip code/coordinates

  def GeoDL(client,path):
  # Create Geo report query.
  report_query = ('SELECT Criteria, CampaignName, AdGroupName, Impressions, '
                  'Clicks, Cost, Conversions '
                  'FROM PLACEMENT_PERFORMANCE_REPORT '
                  'WHERE Clicks > 0 '
                  'DURING 20160725,20160918')

  with open(path, 'w') as output_file:
    report_downloader.DownloadReportWithAwql(
        report_query, 'CSV', output_file, skip_report_header=False,
        skip_column_header=False, skip_report_summary=False)

"""

def compileCampStats(path):
  # Compile campaign level Adwords metrics
  df = pd.read_csv(path,skiprows=[0])
  df.head()
  table = pd.pivot_table(df,index="Campaign",values=["Impressions","Clicks","CTR",
    "Avg. CPC", "Cost","Conversions"],aggfunc=np.sum)
  '''replaced with direct query 
  table['CTR'] = table['Clicks']/table['Impressions']
  table['Avg. CPC'] = (table['Cost']/1000000)/table['Clicks']'''
  table['RealCost'] = table['Cost']/1000000
  #table['Cost Per Conv'] = (table['Cost']/1000000)/table["Conversions"]
  #table['Conversion Rate'] = table["Conversions"]/table['Clicks']
  table.to_excel(writer,sheet_name='CampaignStats')

def compileCampDeviceStats(path):
  # Compile campaign level Adwords metrics segmented by device
  df = pd.read_csv(path,skiprows=[0])
  df.head()
  table = pd.pivot_table(df,index=["Campaign","Device"], values=["Impressions",
    "Clicks","CTR","Cost","Conversions",],aggfunc={"Impressions":np.sum,
    "Clicks":np.sum,"CTR":np.mean, "Cost":np.sum, "Conversions":np.sum,
    "Avg. position":np.mean})
  table['CTR'] = table['Clicks']/table['Impressions']
  table['RealCost'] = table['Cost']/1000000
  table['Avg. CPC'] = table['RealCost']/table['Clicks']
  #table['Cost Per Conv'] = table['RealCost']/table['Conversions']
  #table['Conversion Rate'] = table['Conversions']/table['Clicks']
  table.to_excel(writer,sheet_name="DeviceStats")

def compileGroupStats(path):
  # Compile group level Adwords metrics
  df = pd.read_csv(path,skiprows=[0])
  df.head()
  # deprecated single aggfuncs and concat to attempt single pass with aggfunc dict, see below
  #table1 = pd.pivot_table(df,index=["AdGroupName"], values=["Impressions","Clicks",
    #"Cost","Conversions"],aggfunc=np.sum)
  #table2 = pd.pivot_table(df,index=["AdGroupName"], values=["AveragePosition"],aggfunc=np.mean)
  #table = pd.concat((df1, df2), axis=1)
  table = pd.pivot_table(df,index=["Campaign","Ad group"], values=["Impressions","Clicks",
    "Cost","Conversions","Avg. position"],aggfunc={"Impressions":np.sum,"Clicks":np.sum,"Cost":np.sum,
    "Conversions":np.sum,"Avg. position":np.mean})
  table['CTR'] = table['Clicks']/table['Impressions']
  table['RealCost'] = table['Cost']/1000000
  #table['Cost Per Conv'] = table['RealCost']/table['Conversions']
  #table['Conversion Rate'] = table['Conversions']/table['Clicks']
  table.to_excel(writer,sheet_name="GroupStats")

def compilePlacementStats(path):
  # Compile placement level Adwords metrics
  df = pd.read_csv(path,skiprows=[0])
  df.head()
  table = pd.pivot_table(df,index=["Campaign", "Ad group", "Placement"], values=["Impressions",
    "Clicks","Cost","Conversions"],aggfunc=np.sum)
  table.to_excel(writer,sheet_name="PlacementStats")

def compileKeywordStats(path):
  # Compile keyword level Adwords metrics
  df = pd.read_csv(path,skiprows=[0])
  df.head()
  table = pd.pivot_table(df,index=["Keyword","Match type", "Keyword state", "Campaign", "Ad group"], values=["Impressions",
    "Clicks","Cost","Conversions"],aggfunc=np.sum)
  table['CTR'] = table['Clicks']/table['Impressions']
  table['RealCost'] = table['Cost']/1000000
  table['Avg. CPC'] = table['RealCost']/table['Clicks']
  #table['Cost Per Conv'] = table['RealCost']/table['Conversions']
  #table['Conversion Rate'] = table['Conversions']/table['Clicks']
  table.to_excel(writer,sheet_name="KeywordStats")



if __name__ == '__main__':
  # Initialize Adwords client object and writer object.
  adwords_client = adwords.AdWordsClient.LoadFromStorage()
  writer = pd.ExcelWriter('ADRStats.xlsx', engine='xlsxwriter')


  # Download and compile stats for Campaign and Device tabs
  campaignDL(adwords_client, campaignsPath)
  compileCampStats(campaignsPath)
  compileCampDeviceStats(campaignsPath)

  # Download and compile stats for Groups tab
  groupDL(adwords_client, groupsPath)
  compileGroupStats(groupsPath)

  # Download and compile stats for Placements tab
  placementsDL(adwords_client, placementsPath)
  compilePlacementStats(placementsPath)

  # Download and compile states for Keywords tab
  keywordsDL(adwords_client, keywordsPath)
  compileKeywordStats(keywordsPath)

  # Save/close the writer object and output the Excel file
  writer.save()
