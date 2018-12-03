game_play_template_1 = {
                        "document": {
                            "type": "APL",
                            "version": "1.0",
                            "theme": "dark",
                            "import": [
                                {
                                    "name": "alexa-layouts",
                                    "version": "1.0.0"
                                }
                            ],
                            "resources": [
                                {
                                    "description": "Stock color for the light theme",
                                    "colors": {
                                        "colorTextPrimary": "#151920"
                                    }
                                },
                                {
                                    "description": "Stock color for the dark theme",
                                    "when": "${viewport.theme == 'dark'}",
                                    "colors": {
                                        "colorTextPrimary": "#f0f1ef"
                                    }
                                },
                                {
                                    "description": "Standard font sizes",
                                    "dimensions": {
                                        "textSizeBody": 48,
                                        "textSizePrimary": 27,
                                        "textSizeSecondary": 23,
                                        "textSizeSecondaryHint": 25
                                    }
                                },
                                {
                                    "description": "Common spacing values",
                                    "dimensions": {
                                        "spacingThin": 6,
                                        "spacingSmall": 12,
                                        "spacingMedium": 24,
                                        "spacingLarge": 48,
                                        "spacingExtraLarge": 72
                                    }
                                },
                                {
                                    "description": "Common margins and padding",
                                    "dimensions": {
                                        "marginTop": 40,
                                        "marginLeft": 60,
                                        "marginRight": 60,
                                        "marginBottom": 40
                                    }
                                }
                            ],
                            "styles": {
                                "textStyleBase": {
                                    "description": "Base font description; set color and core font family",
                                    "values": [
                                        {
                                            "color": "@colorTextPrimary",
                                            "fontFamily": "Amazon Ember"
                                        }
                                    ]
                                },
                                "textStyleBase0": {
                                    "description": "Thin version of basic font",
                                    "extend": "textStyleBase",
                                    "values": {
                                        "fontWeight": "100"
                                    }
                                },
                                "textStyleBase1": {
                                    "description": "Light version of basic font",
                                    "extend": "textStyleBase",
                                    "values": {
                                        "fontWeight": "300"
                                    }
                                },
                                "mixinBody": {
                                    "values": {
                                        "fontSize": "@textSizeBody"
                                    }
                                },
                                "mixinPrimary": {
                                    "values": {
                                        "fontSize": "@textSizePrimary"
                                    }
                                },
                                "mixinSecondary": {
                                    "values": {
                                        "fontSize": "@textSizeSecondary"
                                    }
                                },
                                "textStylePrimary": {
                                    "extend": [
                                        "textStyleBase1",
                                        "mixinPrimary"
                                    ]
                                },
                                "textStyleSecondary": {
                                    "extend": [
                                        "textStyleBase0",
                                        "mixinSecondary"
                                    ]
                                },
                                "textStyleBody": {
                                    "extend": [
                                        "textStyleBase1",
                                        "mixinBody"
                                    ]
                                },
                                "textStyleSecondaryHint": {
                                    "values": {
                                        "fontFamily": "Bookerly",
                                        "fontStyle": "italic",
                                        "fontSize": "@textSizeSecondaryHint",
                                        "color": "@colorTextPrimary"
                                    }
                                }
                            },
                            "layouts": {},
                            "mainTemplate": {
                                "parameters": [
                                    "payload"
                                ],
                                "items": [
                                    {
                                        "when": "${viewport.shape == 'round'}",
                                        "type": "Container",
                                        "direction": "column",
                                        "width": "100vw",
                                        "height": "100vh",
                                        "items": [
                                            {
                                                "type": "Image",
                                                "source": "${payload.bodyTemplate3Data.image.sources[0].url}",
                                                "scale": "best-fill",
                                                "width": "100vw",
                                                "height": "100vh",
                                                "position": "absolute",
                                                "overlayColor": "rgba(0, 0, 0, 0.6)",
                                                "scrim": true
                                            },
                                            {
                                                "type": "ScrollView",
                                                "width": "100vw",
                                                "height": "100vh",
                                                "item": [
                                                    {
                                                        "type": "Container",
                                                        "direction": "column",
                                                        "alignItems": "center",
                                                        "paddingLeft": 30,
                                                        "paddingRight": 30,
                                                        "paddingBottom": 200,
                                                        "items": [
                                                            {
                                                                "type": "AlexaHeader",
                                                                "headerAttributionImage": "${payload.bodyTemplate3Data.logoUrl}",
                                                                "headerTitle": "${payload.bodyTemplate3Data.title}"
                                                            },
                                                            {
                                                                "type": "Text",
                                                                "text": "<b>Food pairings</b> | <b>Wine pairings</b>",
                                                                "style": "textStylePrimary",
                                                                "color": "#4dd2ff",
                                                                "width": "90vw",
                                                                "textAlign": "center"
                                                            },
                                                            {
                                                                "type": "Text",
                                                                "text": "<b>${payload.bodyTemplate3Data.textContent.title.text}</b>",
                                                                "style": "textStyleBody",
                                                                "width": "90vw",
                                                                "textAlign": "center"
                                                            },
                                                            {
                                                                "type": "Text",
                                                                "text": "${payload.bodyTemplate3Data.textContent.subtitle.text}",
                                                                "style": "textStylePrimary",
                                                                "width": "90vw",
                                                                "textAlign": "center"
                                                            },
                                                            {
                                                                "type": "Text",
                                                                "text": "${payload.bodyTemplate3Data.textContent.bulletPoint.text}",
                                                                "paddingTop": 50,
                                                                "style": "textStylePrimary",
                                                                "width": "90vw",
                                                                "textAlign": "center"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "type": "Container",
                                        "width": "100vw",
                                        "height": "100vh",
                                        "items": [
                                            {
                                                "type": "Image",
                                                "source": "${payload.bodyTemplate3Data.backgroundImage.sources[0].url}",
                                                "scale": "best-fill",
                                                "width": "100vw",
                                                "height": "100vh",
                                                "position": "absolute",
                                                "overlayColor": "rgba(0, 0, 0, 0.3)"
                                            },
                                            {
                                                "type": "AlexaHeader",
                                                "headerTitle": "${payload.bodyTemplate3Data.title} \\t\\t\\t Remaining Undo: ${payload.bodyTemplate3Data.textContent.remaining_undo_count}",
                                                "headerAttributionImage": "${payload.bodyTemplate3Data.logoUrl}"
                                            },
                                            {
                                                "type": "Container",
                                                "direction": "row",
                                                "paddingLeft": 40,
                                                "paddingRight": 72,
                                                "grow": 1,
                                                "items": [
                                                    {
                                                        "type": "Image",
                                                        "source": "${payload.bodyTemplate3Data.image.sources[0].url}",
                                                        "width": 340,
                                                        "height": 340,
                                                        "scale": "best-fit",
                                                        "align": "center"
                                                    },
                                                    {
                                                        "type": "ScrollView",
                                                        "scrollDirection": "vertical",
                                                        "height": "50vh",
                                                        "shrink": 1,
                                                        "paddingLeft": 20,
                                                        "item": [
                                                            {
                                                                "type": "Container",
                                                                "items": [
                                                                    {
                                                                        "type": "Text",
                                                                        "text": "<b>Your Score: ${payload.bodyTemplate3Data.textContent.score.your_score}</b>",
                                                                        "color": "#4dd2ff"
                                                                    },
                                                                    {
                                                                        "type": "Text",
                                                                        "text": "<b>Your High Score: ${payload.bodyTemplate3Data.textContent.score.your_score}</b>",
                                                                        "color": "#4dd2ff"
                                                                    },
                                                                    {
                                                                        "type": "Text",
                                                                        "text": "<b>High Score: ${payload.bodyTemplate3Data.textContent.score.your_score}</b>",
                                                                        "color": "#4dd2ff"
                                                                    },
                                                                    {
                                                                        "type": "Text",
                                                                        "text": "<b>AI BOT: ${payload.bodyTemplate3Data.textContent.prediction}</b>",
                                                                        "style": "textStyleBody"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "Container",
                                                "direction": "row",
                                                "item": [
                                                    {
                                                        "type": "Image",
                                                        "source": "${payload.bodyTemplate3Data.advertisement.url}",
                                                        "width": 1024,
                                                        "height": 150,
                                                        "scale": "best-fit",
                                                        "align": "center"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        },
                        "dataSources": {
                            "bodyTemplate3Data": {
                                "type": "object",
                                "objectId": "bt3Sample",
                                "backgroundImage": {
                                    "contentDescription": null,
                                    "smallSourceUrl": null,
                                    "largeSourceUrl": null,
                                    "sources": [
                                        {
                                            "url": "https://s3-eu-west-1.amazonaws.com/2048gameyash/Permanent_images/background.png",
                                            "size": "small",
                                            "widthPixels": 0,
                                            "heightPixels": 0
                                        },
                                        {
                                            "url": "https://s3-eu-west-1.amazonaws.com/2048gameyash/Permanent_images/background.png",
                                            "size": "large",
                                            "widthPixels": 0,
                                            "heightPixels": 0
                                        }
                                    ]
                                },
                                "title": "1st Game",
                                "image": {
                                    "contentDescription": null,
                                    "smallSourceUrl": null,
                                    "largeSourceUrl": null,
                                    "sources": [
                                        {
                                            "url": "https://s3-eu-west-1.amazonaws.com/2048gameyash/left.png",
                                            "size": "small",
                                            "widthPixels": 0,
                                            "heightPixels": 0
                                        },
                                        {
                                            "url": "https://s3-eu-west-1.amazonaws.com/2048gameyash/left.png",
                                            "size": "large",
                                            "widthPixels": 0,
                                            "heightPixels": 0
                                        }
                                    ]
                                },
                                "advertisement": {
                                    "type": "flat",
                                    "url": "https://s3-eu-west-1.amazonaws.com/2048gameyash/add4.png"
                                },
                                "textContent": {
                                    "title": {
                                        "type": "PlainText",
                                        "text": "Mild Gouda"
                                    },
                                    "score": {
                                        "your_score": null,
                                        "your_high_score": null,
                                        "high_score": null
                                    },
                                    "prediction": "comming soon",
                                    "remaining_undo_count": 0,
                                    "subtitle": {
                                        "type": "PlainText",
                                        "text": "Country of origin: Netherlands"
                                    },
                                    "primaryText": {
                                        "type": "PlainText",
                                        "text": "Mild Gouda is a semi hard cheese with a creamy texture and mild nutty flavor. Easy to cut and grate, it also melts beautifully. Gouda is a Dutch yellow cheese made from cow's milk, and one of the most popular cheeses worldwide. "
                                    },
                                    "bulletPoint": {
                                        "type": "PlainText",
                                        "text": "• The cheese is named after the Dutch city of Gouda. "
                                    }
                                },
                                "logoUrl": "https://s3-eu-west-1.amazonaws.com/2048gameyash/Permanent_images/logo.png",
                                "hintText": "Try, \"Alexa, search for blue cheese\""
                            }
                        }
                    }