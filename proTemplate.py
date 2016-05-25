# import inspect,os # path to file
# directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
import uuid
def headerTemplate():
	return '''<RVPresentationDocument height="1080" width="1920" versionNumber="500" docType="0" creatorCode="1349676880" lastDateUsed="2016-03-26T04:07:20" usedCount="0" category="Presentation" resourcesDirectory="" backgroundColor="0 0 0 1" drawingBackgroundColor="0" notes="" artist="" author="" album="" CCLIDisplay="0" CCLIArtistCredits="" CCLISongTitle="" CCLIPublisher="" CCLICopyrightInfo="" CCLILicenseNumber="" chordChartPath="">
	<timeline timeOffSet="0" selectedMediaTrackIndex="0" unitOfMeasure="60" duration="0" loop="0">
		<timeCues containerClass="NSMutableArray"/>
		<mediaTracks containerClass="NSMutableArray"/>
	</timeline>
	<bibleReference containerClass="NSMutableDictionary"/>
	<_-RVProTransitionObject-_transitionObject transitionType="-1" transitionDuration="1" motionEnabled="0" motionDuration="20" motionSpeed="100"/>
	<groups containerClass="NSMutableArray">
		<RVSlideGrouping name="" uuid="'''+str(uuid.uuid4())+'''" color="0 0 0 0" serialization-array-index="0">
			<slides containerClass="NSMutableArray">'''

	

def footerTemplate():
	return '''</slides>
		</RVSlideGrouping>
	</groups>
	<arrangements containerClass="NSMutableArray">
		<RVSongArrangement name="New Arrangement" uuid="'''+str(uuid.uuid4())+'''" color="0 0 0 0" serialization-array-index="0">
			<groupIDs containerClass="NSMutableArray">
				<NSMutableString serialization-native-value="'''+str(uuid.uuid4())+'''" serialization-array-index="0"/>
			</groupIDs>
		</RVSongArrangement>
	</arrangements>
</RVPresentationDocument>'''

def slideTemplate(userName, captionText, imagePath, userImagePath):
	return '''<RVDisplaySlide backgroundColor="0 0 0 1" enabled="1" highlightColor="" hotKey="" label="" notes="" slideType="1" sort_index="0" UUID="'''+str(uuid.uuid4())+'''" drawingBackgroundColor="0" chordChartPath="" serialization-array-index="0">
					<cues containerClass="NSMutableArray"/>
					<displayElements containerClass="NSMutableArray">
					<!-- Caption Text -->
					
						<RVTextElement displayDelay="0" displayName="Default" locked="0" persistent="0" typeID="0" fromTemplate="1" bezelRadius="0" drawingFill="0" drawingShadow="1" drawingStroke="0" fillColor="0 0 0 0" rotation="0" source="" adjustsHeightToFit="0" verticalAlignment="0" RTFData="'''+captionText+'''" revealType="0" serialization-array-index="0">
							<_-RVRect3D-_position x="278.25" y="954.2449" z="0" width="1242.962" height="67.62628"/>
							<_-D-_serializedShadow containerClass="NSMutableDictionary">
								<NSMutableString serialization-native-value="{2.8284297, -2.8284297}" serialization-dictionary-key="shadowOffset"/>
								<NSNumber serialization-native-value="4" serialization-dictionary-key="shadowBlurRadius"/>
								<NSColor serialization-native-value="0 0 0 1" serialization-dictionary-key="shadowColor"/>
							</_-D-_serializedShadow>
							<stroke containerClass="NSMutableDictionary">
								<NSColor serialization-native-value="0 0 0 0" serialization-dictionary-key="RVShapeElementStrokeColorKey"/>
								<NSNumber serialization-native-value="0" serialization-dictionary-key="RVShapeElementStrokeWidthKey"/>
							</stroke>
						</RVTextElement>
						
						<!-- Image From Instagram -->
						<RVTextElement displayDelay="0" displayName="Default" locked="0" persistent="0" typeID="0" fromTemplate="1" bezelRadius="0" drawingFill="0" drawingShadow="1" drawingStroke="0" fillColor="0 0 0 0" rotation="0" source="" adjustsHeightToFit="0" verticalAlignment="0" RTFData="e1xydGYxXGFuc2lcYW5zaWNwZzEyNTJcY29jb2FydGYxMzQ4XGNvY29hc3VicnRmMTcwClxjb2NvYXNjcmVlbmZvbnRzMXtcZm9udHRibFxmMFxmc3dpc3NcZmNoYXJzZXQwIEhlbHZldGljYS1MaWdodDt9CntcY29sb3J0Ymw7XHJlZDI1NVxncmVlbjI1NVxibHVlMjU1O30KXHBhcmRcdHg1NjBcdHgxMTIwXHR4MTY4MFx0eDIyNDBcdHgyODAwXHR4MzM2MFx0eDM5MjBcdHg0NDgwXHR4NTA0MFx0eDU2MDBcdHg2MTYwXHR4NjcyMFxwYXJkaXJuYXR1cmFsXHFjCgpcZjBcZnM2NCBcY2YxIFxleHBuZDBcZXhwbmR0dzBca2VybmluZzAKXG91dGwwXHN0cm9rZXdpZHRoLTIwIFxzdHJva2VjMCBJbWFnZSBmcm9tIEluc3RhZ3JhbX0=" revealType="0" serialization-array-index="1">
							<_-RVRect3D-_position x="1354.25" y="921.1875" z="0" width="760.77" height="200.6786"/>
							<_-D-_serializedShadow containerClass="NSMutableDictionary">
								<NSMutableString serialization-native-value="{2.8284297, -2.8284297}" serialization-dictionary-key="shadowOffset"/>
								<NSNumber serialization-native-value="4" serialization-dictionary-key="shadowBlurRadius"/>
								<NSColor serialization-native-value="0 0 0 1" serialization-dictionary-key="shadowColor"/>
							</_-D-_serializedShadow>
							<stroke containerClass="NSMutableDictionary">
								<NSColor serialization-native-value="0 0 0 0" serialization-dictionary-key="RVShapeElementStrokeColorKey"/>
								<NSNumber serialization-native-value="0" serialization-dictionary-key="RVShapeElementStrokeWidthKey"/>
							</stroke>
						</RVTextElement>

						<!-- user image path -->
						<RVImageElement displayDelay="0" displayName="" locked="0" persistent="0" typeID="0" fromTemplate="0" bezelRadius="0" drawingFill="0" drawingShadow="0" drawingStroke="0" fillColor="1 1 1 1" rotation="0" source="file://localhost'''+userImagePath+'''" flippedHorizontally="0" flippedVertically="0" scaleFactor="0.08435909" serializedImageOffset="0.000000@0.000000" serializedFilters="YnBsaXN0MDDUAQIDBAUIFhdUJHRvcFgkb2JqZWN0c1gkdmVyc2lvblkkYXJjaGl2ZXLRBgdUcm9vdIABowkKD1UkbnVsbNILDA0OViRjbGFzc1pOUy5vYmplY3RzgAKg0hAREhNYJGNsYXNzZXNaJGNsYXNzbmFtZaMTFBVeTlNNdXRhYmxlQXJyYXlXTlNBcnJheVhOU09iamVjdBIAAYagXxAPTlNLZXllZEFyY2hpdmVyCBEWHygyNTo8QEZLUl1fYGVueX2MlJ2iAAAAAAAAAQEAAAAAAAAAGAAAAAAAAAAAAAAAAAAAALQ=" scaleBehavior="0" brightness="0" contrast="1" saturation="1" hue="0" manufactureURL="" manufactureName="" format="Portable Network Graphics image" enableColorFilter="0" colorFilter="1 0 0 1" enableBlur="0" blurRadius="0" enableEdgeBlur="0" edgeBlurRadius="0" edgeBlurArea="0" enableSepia="0" enableColorInvert="0" enableGrayInvert="0" enableHeatSignature="0" serialization-array-index="2">
							<_-RVRect3D-_position x="59" y="902.8156" z="0" width="193.1465" height="108.0303"/>
							<_-D-_serializedShadow containerClass="NSMutableDictionary">
								<NSMutableString serialization-native-value="{5, -5}" serialization-dictionary-key="shadowOffset"/>
								<NSNumber serialization-native-value="0" serialization-dictionary-key="shadowBlurRadius"/>
								<NSColor serialization-native-value="0 0 0 0.3333333432674408" serialization-dictionary-key="shadowColor"/>
							</_-D-_serializedShadow>
							<stroke containerClass="NSMutableDictionary">
								<NSColor serialization-native-value="0 0 0 1" serialization-dictionary-key="RVShapeElementStrokeColorKey"/>
								<NSNumber serialization-native-value="1" serialization-dictionary-key="RVShapeElementStrokeWidthKey"/>
							</stroke>
						</RVImageElement>

						<!-- image -->
						<RVImageElement displayDelay="0" displayName="" locked="0" persistent="0" typeID="0" fromTemplate="0" bezelRadius="0" drawingFill="0" drawingShadow="0" drawingStroke="0" fillColor="1 1 1 1" rotation="0" source="file://localhost'''+imagePath+'''" flippedHorizontally="0" flippedVertically="0" scaleFactor="2.190971" serializedImageOffset="0.000000@0.000000" serializedFilters="YnBsaXN0MDDUAQIDBAUIFhdUJHRvcFgkb2JqZWN0c1gkdmVyc2lvblkkYXJjaGl2ZXLRBgdUcm9vdIABowkKD1UkbnVsbNILDA0OViRjbGFzc1pOUy5vYmplY3RzgAKg0hAREhNYJGNsYXNzZXNaJGNsYXNzbmFtZaMTFBVeTlNNdXRhYmxlQXJyYXlXTlNBcnJheVhOU09iamVjdBIAAYagXxAPTlNLZXllZEFyY2hpdmVyCBEWHygyNTo8QEZLUl1fYGVueX2MlJ2iAAAAAAAAAQEAAAAAAAAAGAAAAAAAAAAAAAAAAAAAALQ=" scaleBehavior="0" brightness="0" contrast="1" saturation="1" hue="0" manufactureURL="" manufactureName="" format="Portable Network Graphics image" enableColorFilter="0" colorFilter="1 0 0 1" enableBlur="0" blurRadius="0" enableEdgeBlur="0" edgeBlurRadius="0" edgeBlurArea="0" enableSepia="0" enableColorInvert="0" enableGrayInvert="0" enableHeatSignature="0" serialization-array-index="3">
							<_-RVRect3D-_position x="48.96661" y="23" z="0" width="1822.067" height="845.7147"/>
							<_-D-_serializedShadow containerClass="NSMutableDictionary">
								<NSMutableString serialization-native-value="{5, -5}" serialization-dictionary-key="shadowOffset"/>
								<NSNumber serialization-native-value="0" serialization-dictionary-key="shadowBlurRadius"/>
								<NSColor serialization-native-value="0 0 0 0.3333333432674408" serialization-dictionary-key="shadowColor"/>
							</_-D-_serializedShadow>
							<stroke containerClass="NSMutableDictionary">
								<NSColor serialization-native-value="0 0 0 1" serialization-dictionary-key="RVShapeElementStrokeColorKey"/>
								<NSNumber serialization-native-value="1" serialization-dictionary-key="RVShapeElementStrokeWidthKey"/>
							</stroke>
						</RVImageElement>
						<!-- Username Text -->
						
						<RVTextElement displayDelay="0" displayName="Default" locked="0" persistent="0" typeID="0" fromTemplate="1" bezelRadius="0" drawingFill="0" drawingShadow="1" drawingStroke="0" fillColor="0 0 0 0" rotation="0" source="" adjustsHeightToFit="0" verticalAlignment="0" RTFData="'''+userName+'''" revealType="0" serialization-array-index="4">
							<_-RVRect3D-_position x="276.25" y="894.2449" z="0" width="494.8838" height="67.62628"/>
							<_-D-_serializedShadow containerClass="NSMutableDictionary">
								<NSMutableString serialization-native-value="{2.8284299, -2.8284299}" serialization-dictionary-key="shadowOffset"/>
								<NSNumber serialization-native-value="4" serialization-dictionary-key="shadowBlurRadius"/>
								<NSColor serialization-native-value="0 0 0 1" serialization-dictionary-key="shadowColor"/>
							</_-D-_serializedShadow>
							<stroke containerClass="NSMutableDictionary">
								<NSColor serialization-native-value="0 0 0 0" serialization-dictionary-key="RVShapeElementStrokeColorKey"/>
								<NSNumber serialization-native-value="0" serialization-dictionary-key="RVShapeElementStrokeWidthKey"/>
							</stroke>
						</RVTextElement>
					</displayElements>
					<_-RVProTransitionObject-_transitionObject transitionType="-1" transitionDuration="1" motionEnabled="0" motionDuration="20" motionSpeed="100"/>
				</RVDisplaySlide>'''
